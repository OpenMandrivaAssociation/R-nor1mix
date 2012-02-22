%global packname  nor1mix
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.1_3
Release:          1
Summary:          Normal (1-d) Mixture Models (S3 Classes and Methods)
Group:            Sciences/Mathematics
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-3.tar.gz
Requires:         R-stats R-graphics R-cluster 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-stats R-graphics R-cluster

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