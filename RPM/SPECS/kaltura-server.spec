Summary: Kaltura Open Source Video Platform all in 1 package 
Name: kaltura-server
Version: 9.7.0
Release: 1
License: AGPLv3+
Group: Server/Platform 
URL: http://kaltura.org
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch: noarch
Requires: kaltura-front, kaltura-batch, kaltura-sphinx, kaltura-dwh

%description
Kaltura is the world's first Open Source Online Video Platform, transforming the way people work, 
learn, and entertain using online video. 
The Kaltura platform empowers media applications with advanced video management, publishing, 
and monetization tools that increase their reach and monetization and simplify their video operations. 
Kaltura improves productivity and interaction among millions of employees by providing enterprises 
powerful online video tools for boosting internal knowledge sharing, training, and collaboration, 
and for more effective marketing. Kaltura offers next generation learning for millions of students and 
teachers by providing educational institutions disruptive online video solutions for improved teaching,
learning, and increased engagement across campuses and beyond. 
For more information visit: http://corp.kaltura.com, http://www.kaltura.org and http://www.html5video.org.

This is a meta package which installs an all in 1 server. i.e: all server nodes will be installed on the same machine, producing a standalone Kaltura server.

%clean
rm -rf %{buildroot}

%post

%preun

%postun

%files

%changelog
* Mon Jan 8 2014 Jess Portnoy <jess.portnoy@kaltura.com> - 9.7.0-1
- This is a meta package which installs an all in 1 server. i.e: all server nodes will be installed on the same machine, producing a standalone Kaltura server.