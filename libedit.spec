Name:		libedit
Version:	3.1
Release:	25
Summary:	The NetBSD Editline library
License:	BSD
URL:		http://www.thrysoee.dk/editline/

Source0:	libedit-20170329-3.1.tar.gz
BuildRequires:	gcc, ncurses-devel

%description
Libedit is the automatic tool and libtoolized port of the NetBSD Editline library.
It provides generic line editing, history, and markup functions similar to
those in GNU Readline.

%package devel
Summary:	libedit's development files
Requires:	%{name} = %{version}-%{release}
Requires:	ncurses-devel%{?_isa}

%description devel
libedit's development files

%package help
Summary:	Help information for user

%description help
Help information for user

%prep
%autosetup -n libedit-20170329-3.1

# below for fixing issue of rpmlint
iconv -f ISO8859-1 -t UTF-8 -o ChangeLog.utf-8 ChangeLog
touch -r ChangeLog ChangeLog.utf-8
mv -f ChangeLog.utf-8 ChangeLog

# delete nroff macro
sed -i 's,\\\*\[Gt\],>,' doc/editline.3.roff

%build
%configure --disable-static --disable-silent-rules
sed -i "s/lncurses/ltinfo/" src/Makefile
sed -i "s/ -lncurses//" libedit.pc
%make_build

%install
%make_install
%ldconfig_scriptlets

%files
%doc COPYING ChangeLog THANKS
%{_libdir}/libedit.so.*

%files devel
%{_includedir}/histedit.h
%{_includedir}/editline/readline.h
%{_libdir}/libedit.so
%{_libdir}/pkgconfig/libedit.pc
%exclude %{_libdir}/*.la

%files help
%doc examples/fileman.c examples/tc1.c examples/wtc1.c
%{_mandir}/man3/*
%{_mandir}/man5/editrc.5*
%{_mandir}/man7/*
%exclude %{_mandir}/man3/history.3*

%changelog
* Wed Sep 4 2019 openEuler Buildteam <buildteam@openeuler.org> - 3.1-25
- Package init
