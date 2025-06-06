<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

<!-- This file is used to hold constants used across several transforms. -->
<!-- Constants are called variables in XSLT.  At this point this is not a surprise. -->

<!-- abbreviated as idents in the XCCDF-->
<xsl:variable name="cceuri">https://ncp.nist.gov/cce</xsl:variable>

<!-- abbreviated as references in the XCCDF-->
<xsl:variable name="anssiuri">https://cyber.gouv.fr/sites/default/files/document/linux_configuration-en-v2.pdf</xsl:variable>
<xsl:variable name="bsiuri">https://www.bsi.bund.de/SharedDocs/Downloads/EN/BSI/Grundschutz/International/bsi_it_gs_comp_2022.pdf</xsl:variable>
<xsl:variable name="cjisd-its-uri">https://www.fbi.gov/file-repository/cjis-security-policy-v5_5_20160601-2-1.pdf</xsl:variable>
<xsl:variable name="cnss1253uri">http://www.cnss.gov/Assets/pdf/CNSSI-1253.pdf</xsl:variable>
<xsl:variable name="dcid63uri">not_officially_available</xsl:variable>
<xsl:variable name="disa-appsrguri">https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=application-servers</xsl:variable>
<xsl:variable name="disa-cciuri">https://public.cyber.mil/stigs/cci/</xsl:variable>
<xsl:variable name="disa-ossrguri">https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=operating-systems%2Cgeneral-purpose-os</xsl:variable>
<xsl:variable name="disa-stigs-apps-appsecurity-dev-uri">https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=app-security%2Capp-security-dev</xsl:variable>
<xsl:variable name="disa-stigs-apps-appserver-uri">https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=app-security%2Capplication-servers</xsl:variable>
<xsl:variable name="disa-stigs-apps-browers-uri">https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=app-security%2Cbrowser-guidance</xsl:variable>
<xsl:variable name="disa-stigs-apps-web-server-uri">https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=app-security%2Cweb-servers</xsl:variable>
<xsl:variable name="disa-stigs-os-mainframe-uri">https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=operating-systems%2Cmainframe</xsl:variable>
<xsl:variable name="disa-stigs-os-unix-linux-uri">https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=operating-systems%2Cunix-linux</xsl:variable>
<xsl:variable name="disa-stigs-virtualization-uri">https://public.cyber.mil/stigs/downloads/?_dl_facet_stigs=operating-systems%2Cvirtualization</xsl:variable>
<xsl:variable name="hipaauri">https://www.gpo.gov/fdsys/pkg/CFR-2007-title45-vol1/pdf/CFR-2007-title45-vol1-chapA-subchapC.pdf</xsl:variable>
<xsl:variable name="iso27001-2013uri">https://www.iso.org/contents/data/standard/05/45/54534.html</xsl:variable>
<xsl:variable name="nist800-171uri">http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-171.pdf</xsl:variable>
<xsl:variable name="nist800-53uri">http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf</xsl:variable>
<xsl:variable name="nistcsfuri">https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04162018.pdf</xsl:variable>
<xsl:variable name="isa-62443-2013uri">https://www.isa.org/products/ansi-isa-62443-3-3-99-03-03-2013-security-for-indu</xsl:variable>
<xsl:variable name="isa-62443-2009uri">https://www.isa.org/products/isa-62443-2-1-2009-security-for-industrial-automat</xsl:variable>
<xsl:variable name="cobit5uri">https://www.isaca.org/resources/cobit</xsl:variable>
<xsl:variable name="cis-cscuri">https://www.cisecurity.org/controls/</xsl:variable>
<xsl:variable name="osppuri">https://www.niap-ccevs.org/Profile/PP.cfm</xsl:variable>
<xsl:variable name="pcidssuri">https://www.pcisecuritystandards.org/documents/PCI_DSS_v3-2-1.pdf</xsl:variable>
<xsl:variable name="nerc-cipuri">https://www.nerc.com/pa/Stand/AlignRep/One%20Stop%20Shop.xlsx</xsl:variable>
<xsl:variable name="ssg-contributors-uri">https://github.com/ComplianceAsCode/content/wiki/Contributors</xsl:variable>

<!-- misc language URI's -->
<xsl:variable name="sceuri">http://open-scap.org/page/SCE</xsl:variable>
<xsl:variable name="ovaluri">http://oval.mitre.org/XMLSchema/oval-definitions-5</xsl:variable>

<xsl:variable name="ociltransitional">ocil-transitional</xsl:variable>
<xsl:variable name="ocil_cs">http://scap.nist.gov/schema/ocil/2</xsl:variable>
<xsl:variable name="ocil_ns">http://scap.nist.gov/schema/ocil/2.0</xsl:variable>
</xsl:stylesheet>
