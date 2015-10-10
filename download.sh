#!/usr/bin/env bash

echo "Fetching Independent Rankings"
curl 'http://www.fantasypros.com/nfl/rankings/qb.php?export=xls' > data/qb
curl 'http://www.fantasypros.com/nfl/rankings/k.php?export=xls' > data/k
curl 'http://www.fantasypros.com/nfl/rankings/dst.php?export=xls' > data/dst
curl 'http://www.fantasypros.com/nfl/rankings/dl.php?export=xls' > data/dl

echo "Fetching Standard Rankings"
curl 'http://www.fantasypros.com/nfl/rankings/rb.php?export=xls' > data/rb
curl 'http://www.fantasypros.com/nfl/rankings/wr.php?export=xls' > data/wr
curl 'http://www.fantasypros.com/nfl/rankings/te.php?export=xls' > data/te
curl 'http://www.fantasypros.com/nfl/rankings/flex.php?export=xls' > data/flex

echo "Fetching PPR Data..."
curl 'http://www.fantasypros.com/nfl/rankings/ppr-rb.php?export=xls' > data/ppr-rb
curl 'http://www.fantasypros.com/nfl/rankings/ppr-wr.php?export=xls' > data/ppr-wr 
curl 'http://www.fantasypros.com/nfl/rankings/ppr-te.php?export=xls' > data/ppr-te
curl 'http://www.fantasypros.com/nfl/rankings/ppr-flex.php?export=xls' > data/ppr-flex