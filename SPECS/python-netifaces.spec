%global pypi_name netifaces

%if 0%{?rhel} > 7
# Disable python2 build by default
%bcond_with python2
%else
%bcond_without python2
%endif

Name:           python-netifaces
Version:        0.10.6
Release:        4%{?dist}
Summary:        Python library to retrieve information about network interfaces 
License:        MIT
URL:            https://pypi.python.org/pypi/netifaces
Source0:        https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz

%if %{with python2}
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
%endif # with python2

%description
This package provides a cross platform API for getting address information
from network interfaces.

%if %{with python2}
%package -n python2-%{pypi_name}
Summary:        Python 2 library to retrieve information about network interfaces
%{?python_provide:%python_provide python2-%{pypi_name}}

%description -n python2-%{pypi_name}
This package provides a cross platform API for getting address information
from network interfaces.
%endif # with python2

%package -n python%{python3_pkgversion}-%{pypi_name}
Summary:        Python %{python3_pkgversion} library to retrieve information about network interfaces
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
This package provides a cross platform API for getting address information
from network interfaces.


%prep
%setup -q -n %{pypi_name}-%{version}


%build
%if %{with python2}
%py2_build
%endif # with python2
%py3_build


%install
%if %{with python2}
%py2_install
%endif # with python2
%py3_install

%if %{with python2}
%files -n python2-%{pypi_name}
%doc README.rst
%{python2_sitearch}/%{pypi_name}-%{version}-*.egg-info/
%{python2_sitearch}/%{pypi_name}.so
%endif # with python2

%files -n python%{python3_pkgversion}-%{pypi_name}
%doc README.rst
%{python3_sitearch}/%{pypi_name}-%{version}-*.egg-info/
%{python3_sitearch}/%{pypi_name}*.so

%changelog
* Tue Jun 19 2018 Charalampos Stratakis <cstratak@redhat.com> - 0.10.6-4
- Conditionalize the python2 subpackage

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Jan 26 2018 Iryna Shcherbina <ishcherb@redhat.com> - 0.10.6-2
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Mon Aug 14 2017 Peter Robinson <pbrobinson@fedoraproject.org> 0.10.6-1
- Update to 0.10.6

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Dec 22 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.5-4
- Rebuild for Python 3.6

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 0.10.5-3
- Rebuild for Python 3.6

* Mon Nov 14 2016 Orion Poplawski <orion@cora.nwra.com> - 0.10.5-2
- Really ship python2-netifaces

* Mon Nov 14 2016 Orion Poplawski <orion@cora.nwra.com> - 0.10.5-1
- Update to 0.10.5
- Ship python2-netifaces
- Modernize spec

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.4-5
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.10.4-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Tue Nov 10 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.10.4-3
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Tue Jun 16 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.4-2
- Add python3 subpackage

* Mon Feb 23 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 0.10.4-1
- Upstream 0.10.4
- Packaging cleanups

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Toshio Kuratomi <toshio@fedoraproject.org> - 0.5-7
- Replace python-setuptools-devel BR with python-setuptools

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Jun 1 2011 Ryan Rix <ry@n.rix.si> 0.5-1
- Initial packaging effort
