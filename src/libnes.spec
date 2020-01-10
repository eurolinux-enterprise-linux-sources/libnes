Name: libnes
Version: 1.1.3
Release: 1
Summary: NetEffect Ethernet Server Cluster Adapter Userspace Library

Group: System Environment/Libraries
License: GPL/BSD
Url: http://www.openfabrics.org/
Source: http://www.openfabrics.org/downloads/libnes-1.1.3.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: libibverbs-devel

%description
libnes provides a device-specific userspace library for NetEffect
Ethernet Server Cluster Adaper for use with the libibverbs library.

%package devel-static
Summary: Development files for the libnes library
Group: System Environment/Libraries
Requires: %{name} = %{version}-%{release}

%description devel-static
Static version of libnes that may be linked directly to an
application, which may be useful for debugging.

%prep
%setup -q -n %{name}-1.1.3

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=%{buildroot} install
# remove unpackaged files from the buildroot
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la $RPM_BUILD_ROOT%{_libdir}/libnes.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/libnes*.so
%{_sysconfdir}/libibverbs.d/nes.driver
%doc AUTHORS COPYING gpl-2.0.txt

%files devel-static
%defattr(-,root,root,-)
%{_libdir}/libnes*.a

%changelog
*Fri Nov 21 2011 Faisal Latif <faisal.latif@intel.com> - 1.1.3
- Update for OFED 1.5.4
- Declaration of IBV_QPT_RAW_ETH

*Fri Nov 04 2011 Faisal Latif <faisal.latif@intel.com> - 1.1.2
- Update for OFED 1.5.4
- Fix build against upstream libibverbs

*Wed Dec 15 2010 Faisal Latif <faisal.latif@intel.com> - 1.1.1
- Update for OFED 1.5.3
- Error check when sge > 4 for posting recv buffers
- too long frame error handling
- handling of RAQ QP when in ERR state
- Handing of frames with vlan flag

* Wed Sep 2 2010 Chien Tung <chien.tin.tung@intel.com> - 1.1.0
- Update for OFED 1.5.2.
- Add support for iWarp Multicast Aceleration (IMA).
- Rearm  CQ event notification only after a poll.
- Add option to control doorbell read in nes_upoll_cq.
- Fix total payload calculation in nes_upost_recv.
- Fix Firmware version in query device.

* Wed Mar 3 2010 Chien Tung <chien.tin.tung@intel.com> - 1.0.1
- Update for OFED 1.5.1 RC3.
- Add support for device id 0x0110
- Fix COPYING and gpl-2.0.txt reference

* Tue Dec 8 2009 Chien Tung <chien.tin.tung@intel.com> - 1.0.0
- Update for OFED 1.5 RC4.
- Sync up with libibverbs 1.1.3
- Fix head pointer and fence flag for nes_upost_send and nes_upost_recv

* Wed Oct 14 2009 Chien Tung <chien.tin.tung@intel.com> - 0.9.0
- Updated for OFED-1.5 RC2

* Wed Apr 15 2009 Chien Tung <chien.tin.tung@intel.com> - 0.6
- Updated for OFED-1.4.1

* Wed Aug 29 2007 Glenn Grundstrom <ggrundstrom@neteffect.com> - 0.5
- Updated for OFED-1.3

* Fri Feb 16 2007 Glenn Grundstrom <ggrundstrom@neteffect.com> - 0.3
- Updated for OFED-1.2

* Wed May 10 2006 Glenn Grundstrom <ggrundstrom@neteffect.com> - 0.1
- First development effort
