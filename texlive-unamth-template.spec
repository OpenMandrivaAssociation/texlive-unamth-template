# revision 33625
# category Package
# catalog-ctan /macros/latex/contrib/unamth-template
# catalog-date 2014-04-22 19:24:17 +0200
# catalog-license gpl3
# catalog-version 2.0
Name:		texlive-unamth-template
Version:	2.0
Release:	4
Summary:	UNAM Thesis LaTeX Template
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/unamth-template
License:	GPL3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unamth-template.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/unamth-template.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
The bundle provides a template for UNAM's College of
Engineering Theses. The work is based on Harish Bhanderi's
PhD/MPhil template, and the University of Cambridge Engineering
Department template.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/unamth-template/Agradecimientos/Agradecimientos.tex
%doc %{_texmfdistdir}/doc/latex/unamth-template/Agradecimientos/Dedicatoria.tex
%doc %{_texmfdistdir}/doc/latex/unamth-template/Apendice1/Apendice1.tex
%doc %{_texmfdistdir}/doc/latex/unamth-template/Bibliografia/referencias.bib
%doc %{_texmfdistdir}/doc/latex/unamth-template/Capitulo1/introduccion.tex
%doc %{_texmfdistdir}/doc/latex/unamth-template/Capitulo2/marco_teorico.tex
%doc %{_texmfdistdir}/doc/latex/unamth-template/Capitulo3/diseno_experimento.tex
%doc %{_texmfdistdir}/doc/latex/unamth-template/Capitulo3/figs/planta.jpg
%doc %{_texmfdistdir}/doc/latex/unamth-template/Capitulo4/resultados_y_analisis.tex
%doc %{_texmfdistdir}/doc/latex/unamth-template/Capitulo5/conclusiones.tex
%doc %{_texmfdistdir}/doc/latex/unamth-template/Declaracion/Declaracion.tex
%doc %{_texmfdistdir}/doc/latex/unamth-template/LICENSE
%doc %{_texmfdistdir}/doc/latex/unamth-template/Latex/Classes/CUEDbiblio.bst
%doc %{_texmfdistdir}/doc/latex/unamth-template/Latex/Classes/CUEDthesisPSnPDF.texshop
%doc %{_texmfdistdir}/doc/latex/unamth-template/Latex/Classes/Escudos/fi_azul.pdf
%doc %{_texmfdistdir}/doc/latex/unamth-template/Latex/Classes/Escudos/fi_negro.pdf
%doc %{_texmfdistdir}/doc/latex/unamth-template/Latex/Classes/Escudos/unam_azul.pdf
%doc %{_texmfdistdir}/doc/latex/unamth-template/Latex/Classes/Escudos/unam_azul_5x5cm.pdf
%doc %{_texmfdistdir}/doc/latex/unamth-template/Latex/Classes/Escudos/unam_negro.pdf
%doc %{_texmfdistdir}/doc/latex/unamth-template/Latex/Classes/Escudos/unam_negro_5x5cm.pdf
%doc %{_texmfdistdir}/doc/latex/unamth-template/Latex/Classes/PhDbiblio-bold.bst
%doc %{_texmfdistdir}/doc/latex/unamth-template/Latex/Classes/PhDbiblio-case.bst
%doc %{_texmfdistdir}/doc/latex/unamth-template/Latex/Classes/PhDbiblio-url.bst
%doc %{_texmfdistdir}/doc/latex/unamth-template/Latex/Classes/PhDbiblio-url2.bst
%doc %{_texmfdistdir}/doc/latex/unamth-template/Latex/Classes/PhDthesisPSnPDF.cls
%doc %{_texmfdistdir}/doc/latex/unamth-template/Latex/Classes/urlbst
%doc %{_texmfdistdir}/doc/latex/unamth-template/Latex/Macros/MacroFile1.tex
%doc %{_texmfdistdir}/doc/latex/unamth-template/README.md
%doc %{_texmfdistdir}/doc/latex/unamth-template/Resumen/Resumen.tex
%doc %{_texmfdistdir}/doc/latex/unamth-template/latex_intro.pdf
%doc %{_texmfdistdir}/doc/latex/unamth-template/tesis.pdf
%doc %{_texmfdistdir}/doc/latex/unamth-template/tesis.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
