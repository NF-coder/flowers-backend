#!/bin/bash

python ./Admin.py &
python ./Auth.py &
python ./Catalog.py &
python ./Order.py &
python ./Profile.py &
python ./Supplier.py &

# Wait for any process to exit
wait -n

# Exit with status of process that exited first
exit $?