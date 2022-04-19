# Zowe Support Provider Conformance Guide

Zowe Support Provider Conformance Guide is a set of self-certifying and self-service tests to help support Zowe framework.

This guide describes the requirements of the support conformance program. All Applicants complete sections in the **Core** section. Items marked **(best practice)** are considered best practices.

- [Zowe Support Provider Conformance Guide](#zowe-support-provider-conformance-guide)
  - [Zowe Support Core Section](#zowe-support-core-section)
    - [Zowe Binaries](#zowe-binaries)
    - [Zowe Security](#zowe-security)
    - [Zowe Fix Strategy](#zowe-fix-strategy)
  - [Zowe Support Components Section](#zowe-support-components-section)
    - [Zowe Component Requirements: API Mediation Layer](#zowe-component-requirements-api-mediation-layer)
    - [Zowe Component Requirements: App Framework](#zowe-component-requirements-app-framework)
    - [Zowe Component Requirements: Command Line Interface](#zowe-component-requirements-command-line-interface)
    - [Zowe Component Requirements: Explorer](#zowe-component-requirements-explorer)

## Zowe Support Core Section

### Zowe Binaries

<table rules="all">
 <thead>
  <th style="background-color:#5555AA">Item</th>
  <th style="background-color:#5555AA">Version</th>
  <th style="background-color:#5555AA">Required</th>
  <th style="background-color:#5555AA">Best Practice</th>
  <th style="background-color:#5555AA">Conformant</th>
  <th style="background-color:#5555AA">Criteria</th>
 </thead>
 <tbody>
  <tr>
   <td style="background-color:#555555">1</td>
   <td style="background-color:#555555">v2</td>
   <td style="background-color:#AAAAAA"><center>x</center></td>
   <td style="background-color:#AAAAAA"></td>
   <td></td>
   <td><b>Support Provider agrees:</b> to provide capable support for the given authenticated binary(s) of the Zowe core component(s) being attested to for the version(s) of Zowe defined in this version of the Zowe Support Provider Conformance program.<br />
Capable Support is defined as having necessary hardware, software, and persons to diagnose issues, code solutions, test solutions, and provide fixes for issues in a reasonable timeframe.<br />Zowe core component(s) are defined <a href="https://github.com/zowe/community/blob/master/Technical-Steering-Committee/release.md#the-core-attribute">here</a>.<br />
Authenticated binaries are defined as those applicable to a given Zowe Core component and that passes the verification process (see <a href="https://docs.zowe.org/stable/troubleshoot/verify-fingerprint.html#verify-zowe-runtime-directory">here</a>).</td>
  </tr>
  <tr>
   <td style="background-color:#555555">2</td>
   <td style="background-color:#555555">v2</td>
   <td style="background-color:#AAAAAA"><center>x</center></td>
   <td style="background-color:#AAAAAA"></td>
   <td></td>
   <td><b>Support Provider agrees:</b> to abide by the applicable license associated with the Zowe source code which produced the authenticated binaries.</td>
  </tr>
 </tbody>
</table>

### Zowe Security

<table rules="all">
 <thead>
  <th style="background-color:#5555AA">Item</th>
  <th style="background-color:#5555AA">Version</th>
  <th style="background-color:#5555AA">Required</th>
  <th style="background-color:#5555AA">Best Practice</th>
  <th style="background-color:#5555AA">Conformant</th>
  <th style="background-color:#5555AA">Criteria</th>
 </thead>
 <tbody>
<tr>
  <td style="background-color:#555555">3</td>
  <td style="background-color:#555555">v2</td>
  <td style="background-color:#AAAAAA"><center>x</center></td>
  <td style="background-color:#AAAAAA"></td>
  <td></td>
  <td><b>Support Provider agrees:</b> to follow the Security Reporting Process outlined in the Zowe Docs Report Security Issues section when reporting security vulnerabilities (see <a href="https://docs.zowe.org/stable/contribute/roadmap-contribute.html#report-security-issues">here</a>)</td>
</tr>
</tbody>
</table>

### Zowe Fix Strategy

<table rules="all">
 <thead>
  <th style="background-color:#5555AA">Item</th>
  <th style="background-color:#5555AA">Version</th>
  <th style="background-color:#5555AA">Required</th>
  <th style="background-color:#5555AA">Best Practice</th>
  <th style="background-color:#5555AA">Conformant</th>
  <th style="background-color:#5555AA">Criteria</th>
 </thead>
 <tbody>
  <tr>
   <td style="background-color:#555555">4</td>
   <td style="background-color:#555555">v2</td>
   <td style="background-color:#AAAAAA"><center>x</center></td>
   <td style="background-color:#AAAAAA"></td>
   <td></td>
   <td><b>Support Provider agrees:</b> to the extent that code is contributed upstream to the Zowe project by the Support Provider, the Support Provider would make such contributions adhere to the Zowe project contribution guidelines (see <a href="https://github.com/zowe/community#contribute">here</a>).</td>
  </tr>
  <tr>
   <td style="background-color:#555555">5</td>
   <td style="background-color:#555555">v2</td>
   <td style="background-color:#AAAAAA"><center>x</center></td>
   <td style="background-color:#AAAAAA"></td>
   <td></td>
   <td><b>Support Provider agrees:</b> that it is able to both create and apply emergency fixes to the authenicated binary, including emergency fixes that may come from a third-party. Further, the Support Provider agrees to adhere to any requirements of the applicable license for the emergency fix. An emergency fix is defined as a change made to the components in the authenicated binary to resolve an issue which is deemed urgent or critical for use of the authenicated binary.</td>
  </tr>
 </tbody>
</table>

## Zowe Support Components Section

- **Comprehensive Zowe Support Applicants:** Mark and complete ALL sections below
- **Partial Zowe Support Applicants:** Mark and complete just the sections applicable to your Support Offering
  - [ ] Zowe API Mediation Layer
  - [ ] Zowe App Framework
  - [ ] Zowe Command Line Interface
  - [ ] Zowe Explorer

For each of the applicable COMPONENT SECTIONS selected, **Support Provider Applicant confirms Capable Support as defined in item (1)** (mark each applicable section as conformant in "Conformant" column).

### Zowe Component Requirements: API Mediation Layer

<table rules="all">
 <thead>
  <th style="background-color:#5555AA">Item</th>
  <th style="background-color:#5555AA">Version</th>
  <th style="background-color:#5555AA">Required</th>
  <th style="background-color:#5555AA">Best Practice</th>
  <th style="background-color:#5555AA">Conformant</th>
  <th style="background-color:#5555AA">Criteria</th>
 </thead>
 <tbody>
  <tr>
   <td style="background-color:#555555">6</td>
   <td style="background-color:#555555">v2</td>
   <td style="background-color:#AAAAAA"><center>x</center></td>
   <td style="background-color:#AAAAAA"></td>
   <td></td>
   <td> <b>Support Provider confirms:</b> Capable Support as defined in item (1)</td>
  </tr>
  </tbody>
</table>

### Zowe Component Requirements: App Framework

<table rules="all">
 <thead>
  <th style="background-color:#5555AA">Item</th>
  <th style="background-color:#5555AA">Version</th>
  <th style="background-color:#5555AA">Required</th>
  <th style="background-color:#5555AA">Best Practice</th>
  <th style="background-color:#5555AA">Conformant</th>
  <th style="background-color:#5555AA">Criteria</th>
 </thead>
 <tbody>
 <tr>
   <td style="background-color:#555555">7</td>
   <td style="background-color:#555555">v2</td>
   <td style="background-color:#AAAAAA"><center>x</center></td>
   <td style="background-color:#AAAAAA"></td>
   <td></td>
   <td><b>Support Provider confirms:</b> Capable Support as defined in item (1)</td>
 </tr>
 </tbody>
</table>

### Zowe Component Requirements: Command Line Interface

<table rules="all">
 <thead>
  <th style="background-color:#5555AA">Item</th>
  <th style="background-color:#5555AA">Version</th>
  <th style="background-color:#5555AA">Required</th>
  <th style="background-color:#5555AA">Best Practice</th>
  <th style="background-color:#5555AA">Conformant</th>
  <th style="background-color:#5555AA">Criteria</th>
 </thead>
 <tbody>
 <tr>
   <td style="background-color:#555555">8</td>
   <td style="background-color:#555555">v2</td>
   <td style="background-color:#AAAAAA"><center>x</center></td>
   <td style="background-color:#AAAAAA"></td>
   <td></td>
   <td> <b>Support Provider confirms:</b> Capable Support as defined in item (1)</td>
 </tr>
 </tbody>
</table>

### Zowe Component Requirements: Explorer

<table rules="all">
 <thead>
  <th style="background-color:#5555AA">Item</th>
  <th style="background-color:#5555AA">Version</th>
  <th style="background-color:#5555AA">Required</th>
  <th style="background-color:#5555AA">Best Practice</th>
  <th style="background-color:#5555AA">Conformant</th>
  <th style="background-color:#5555AA">Criteria</th>
 </thead>
 <tbody>
 <tr>
   <td style="background-color:#555555">9</td>
   <td style="background-color:#555555">v4</td>
   <td style="background-color:#AAAAAA"><center>x</center></td>
   <td style="background-color:#AAAAAA"></td>
   <td></td>
   <td> <b>Support Provider confirms:</b> Capable Support as defined in item (1)
   </td>
 </tr>
 </tbody>
</table>