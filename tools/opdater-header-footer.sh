#!/bin/sh
# ============================================================
# Kredithjørnet — indsæt header og footer i alle sider
#
# Kør denne, hver gang du har rettet i partials/header.html
# eller partials/footer.html:
#
#     sh tools/opdater-header-footer.sh
#
# Den skriver indholdet direkte ind i alle HTML-sider, så
# menuen vises med det samme uden at vente på JavaScript.
# Kræver ingen installation — awk følger med macOS.
# ============================================================

set -e
cd "$(dirname "$0")/.."
ROOT=$(pwd)

for PART in header footer; do
  if [ ! -f "$ROOT/partials/$PART.html" ]; then
    echo "Mangler partials/$PART.html — stopper."
    exit 1
  fi
done

COUNT=0

find "$ROOT" -name '*.html' -not -path "$ROOT/.git/*" -not -path "$ROOT/partials/*" | while read -r FILE; do
  CHANGED=0
  for PART in header footer; do
    SRC="$ROOT/partials/$PART.html"
    MARK=$(echo "$PART" | tr '[:lower:]' '[:upper:]')

    # Spring filen over, hvis den hverken har et monteringspunkt eller en tidligere indsættelse
    if ! grep -q -e "<div id=\"site-$PART\"></div>" -e "<!-- KH:$MARK" "$FILE"; then
      continue
    fi

    awk -v src="$SRC" -v mount="site-$PART" -v mark="$MARK" '
      BEGIN { skip = 0 }
      {
        line = $0
        gsub(/^[ \t]+|[ \t]+$/, "", line)

        if (skip == 1) {
          if (index($0, "<!-- /KH:" mark " -->") > 0) skip = 0
          next
        }

        if (index($0, "<!-- KH:" mark) > 0) skip = 1
        else if (line != "<div id=\"" mount "\"></div>") { print; next }

        print "<!-- KH:" mark " — indsat af tools/opdater-header-footer.sh. Ret i partials/, ikke her. -->"
        print "<div id=\"" mount "\">"
        while ((getline l < src) > 0) print l
        close(src)
        print "</div>"
        print "<!-- /KH:" mark " -->"
      }
    ' "$FILE" > "$FILE.kh-tmp"

    mv "$FILE.kh-tmp" "$FILE"
    CHANGED=1
  done

  if [ "$CHANGED" = "1" ]; then
    COUNT=$((COUNT + 1))
    echo "  opdateret  ${FILE#$ROOT/}"
  fi
done

echo ""
echo "Færdig. Tjek siden lokalt, og push så ændringerne."
