%global packname  nor1mix
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          1.1.4
Release:          2
Summary:          Normal (1-d) Mixture Models (S3 Classes and Methods)
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              https://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/nor1mix_1.1-4.tar.gz
Requires:         R-stats R-graphics 
Requires:         R-cluster 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-stats R-graphics
BuildRequires:    R-cluster 

%description
Onedimensional Normal Mixture Models Classes, for, e.g., density
estimation or clustering algorithms research and teaching; providing the
widely used Marron-Wand densities, see ?MarronWand.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Fri Feb 17 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1_3-1
+ Revision: 776259
- Import R-nor1mix
- Import R-nor1mix


