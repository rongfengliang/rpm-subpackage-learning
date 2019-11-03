Name: foo
Version: 2.7
Release: 1
License: apache
Summary: dalong demo rpm subpacakge
Group: dalong/dalong
%description
This is the long description of the foo app, and the baz library needed to
build it...

%package server
Summary: The foo server
Group: dalong/dalong
%description server
This is the long description for the foo server...

%package client
Summary: The foo client
Group: dalong/dalong
%description client
This is the long description for the foo client...

%package -n bazlib
Version: 5.6
Summary: The baz library
Group: dalong/dalong
%description -n bazlib
This is the long description for the bazlib...


%pre
echo "This is the foo package preinstall script"


%build

cat > main.sh <<EOF
#!/bin/sh
echo "main"
EOF

cat > server.sh <<EOF
#!/bin/sh
echo "server"
EOF

cat > client.sh <<EOF
#!/bin/sh
echo "client"
EOF

cat > bazlib.sh <<EOF
#!/bin/sh
echo "bazlib"
EOF

%install

mkdir -p %{buildroot}/usr/local/
install -m 755 main.sh %{buildroot}/usr/local/main.sh
install -m 755 server.sh %{buildroot}/usr/local/server.sh
install -m 755 client.sh %{buildroot}/usr/local/client.sh
install -m 755 bazlib.sh %{buildroot}/usr/local/bazlib.sh

%pre server
echo "This is the foo-server subpackage preinstall script"

%pre client
echo "This is the foo-client subpackage preinstall script"



%pre -n bazlib
echo "This is the bazlib subpackage preinstall script"

%files
/usr/local/main.sh

%files server
/usr/local/server.sh

%files client
/usr/local/client.sh

%files -n bazlib
/usr/local/bazlib.sh