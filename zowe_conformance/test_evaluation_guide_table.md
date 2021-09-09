# Zowe Conformance Test Evaluation Guide

The Zowe Conformance Test Evaluation Guide is a set of self-certifying and self-service tests to help the development community integrate and extend specific technology into the Zowe framework. 

This guide describes the requirements of the three available conformance programs. Items marked **(required)** are required for an application to be conformant. Items marked **(best practice)** are considered best practices for conformant applications.

These Zowe Conformance criteria are applicable to the lastest Zowe v1 LTS Release.

- [Zowe Conformance Test Evaluation Guide](#zowe-conformance-test-evaluation-guide)
  - [Zowe API Mediation Layer - Zowe v1](#zowe-api-mediation-layer---zowe-v1)
    - [Application Service](#application-service)
    - [REST API Documentation](#rest-api-documentation)
    - [REST API Naming and Addressing](#rest-api-naming-and-addressing)
    - [Service Requests and Responses](#service-requests-and-responses)
    - [Authentication and Authorization](#authentication-and-authorization)
    - [Versioning and Support](#versioning-and-support)
    - [WebSocket Services](#websocket-services)
    - [Directory and File Ownership Permissions](#directory-and-file-ownership-permissions)
    - [Lifecycling as a Zowe address space](#lifecycling-as-a-zowe-address-space)
    - [Support](#support)
  - [Zowe CLI - Zowe v1](#zowe-cli---zowe-v1)
    - [Infrastructure](#infrastructure)
    - [Installation](#installation)
    - [Naming](#naming)
    - [Profiles](#profiles)
    - [Support](#support-1)
  - [Zowe App Framework - Zowe v1](#zowe-app-framework---zowe-v1)
    - [Packaging](#packaging)
    - [Web UIs All](#web-uis-all)
    - [Web UI iframe](#web-ui-iframe)
    - [Web UI Non iframe](#web-ui-non-iframe)
    - [UI Design](#ui-design)
    - [Localization and Internationalization l10n and l18n](#localization-and-internationalization-l10n-and-l18n)
    - [App Server](#app-server)
    - [Documentation](#documentation)
    - [Logging](#logging)
    - [Encoding](#encoding)
    - [Storage](#storage)
    - [Directory and File Ownership Permissions](#directory-and-file-ownership-permissions-1)
    - [Lifecycling as a Zowe address space](#lifecycling-as-a-zowe-address-space-1)
    - [Support](#support-2)
  - [Zowe Explorer for VS Code - Zowe v1](#zowe-explorer-for-vs-code---zowe-v1)
    - [General Extension](#general-extension)
    - [Extension Accessing Profiles](#extension-accessing-profiles)
    - [Data Provider Extension](#data-provider-extension)
    - [Extension Adding Menus](#extension-adding-menus)

## Zowe API Mediation Layer - Zowe v1

### Application Service

<table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">1</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The product or applications that extends Zowe API ML must provide at least one API service registered with the Zowe API ML Discovery Service</td>

 </tr>
 <tr>
   <th style="background-color:#555555" rowspan=3>2</th>
   <th style="background-color:#555555"></th>
   <th style="background-color:#AAAAAA" colspan=2>Mark (a) or (b)</th>
   <th style="background-color:#AAAAAA"></th>
   <td style="text-align:center">A service must be registered using one of the following methods:<p style="color:red"> (Mark which one applies _a_ or _b_).</td>

 </tr>
  <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>a. Dynamic Registration</td>

  </tr>
  <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>b. Static Definition</td>

 </tr>
  <tr>
   <th style="background-color:#555555">3</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <td></td>
   <td>The service must provide a default service ID that is prefixed by the organization/provider name.
     <p><b>Examples of compliant service IDs:</b></p><p><code>zowemonitoring, cajclcheck, ibmims, rocketterasam</code></p> <p><b>Examples of non-compliant service IDs:</b></p><p><code>jclcheck, myims, mydb2</code></p><p><b>Note:</b> The API ID is not part of the URL.</p></td>
<tr>

   <th style="background-color:#555555">4</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <td></td>
   <td>The service ID must be configurable externally after deployment</td>

 </tr>
  <tr>
   <th style="background-color:#555555">5</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The service ID must be lower case, contain no symbols, and have a maximum of 64 characters</td>

 <tr>
   <th style="background-color:#555555">6</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
  <td>The API ID must follow the same rules for Java packages. <p><b>Example of the API ID:</b> <code>zowe.apiml.apicatalog</code></p></td>

 </tr>
  <tr>
   <th style="background-color:#555555">7</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The published service URL must follow the gateway URL conventions</td>

 </tr>
<tr>
   <th style="background-color:#555555" rowspan=9>8</th>
   <th style="background-color:#555555"></th>
   <th style="background-color:#AAAAAA" colspan=2>Versioned</th>
   <th style="background-color:#AAAAAA"></th>
   <td style="text-align:center">For versioned APIs, the service URL must contain a service version before the service ID in the following formats:<p style="color:red">(Mark only one section - Versioned or Non-Versioned)</td>

 </tr>
  <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td> - api/v1/{serviceId} reserved for REST APIs</td>
 </tr>
  <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td> - ui/v1/{serviceId} reserved for UIs</td>
 </tr>
   <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td> - ws/v1/{serviceId} reserved for WebSockets</td>
 </tr>
<tr>
   <th style="background-color:#555555"></th>
   <th style="background-color:#AAAAAA" colspan=2>Non-Versioned</th>
   <th style="background-color:#AAAAAA"></th>
   <td>For non-versioned APIs or APIs versioned differently (e.g. z/OSMF), use the following formats:</td>
 </tr>
  <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td> - api/{serviceId} reserved for REST APIs</td>
 </tr>
  <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td> - ui/{serviceId} reserved for UIs</td>
 </tr>
   <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td> - ws/{serviceId} reserved for WebSockets</td>
 </tr>
   <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td> - graphql/{serviceId} reserved for GraphQL APIs</td>
 </tr>

 <tr>
   <th style="background-color:#555555" rowspan=5>9</th>
   <th style="background-color:#555555"></th>
   <th style="background-color:#AAAAAA" colspan=2>Mark (a) or (b) or (c)</th>
   <th style="background-color:#AAAAAA"></th>
   <td style="text-align:center">Registration of the service must not be performed by modifying the Zowe runtime directory api-defs folder. Supported methods include:<p style="color:red">(Mark which one applies _a_, _b_, _c_, or _d_)</td>
 </tr>
  <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
  <td>a. Adding the static API definition YAML file path to <code>instance.env</code> file for the Zowe workspace</td>
 </tr>
  <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td>b. Copying the static API definition YAML file to the instance directory workspace api-definitions directory</td>
 </tr>
   <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
  <td>c. Adding the path of a launch component to the <code>instance.env</code> file for the Zowe workspace</td>
  </tr>
   <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
  <td>d. Dynamic registration of an application that is NOT lifecycled as a Zowe address space /td>
  </tr>

</table>

### REST API Documentation

<table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">10</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Documentation is Swagger/Open API 2.0/Open API 3.0 compliant</td>
 </tr>
 <tr>
   <th style="background-color:#555555">11</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Every public resource is documented with a description of each resource</td>
 </tr>
 <tr>
   <th style="background-color:#555555">12</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Every method of each public REST endpoint is documented</td>
 </tr>
 <tr>
   <th style="background-color:#555555">13</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Every method of each public REST endpoint is demonstrated with an example</td>
 </tr>
 <tr>
   <th style="background-color:#555555">14</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Every parameter (headers, query parameters, payloads, cookies, etc.) is documented with definitions of all possible values and their associated meanings</td>
 </tr>
 <tr>
   <th style="background-color:#555555">15</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Every HTTP error code must be documented. If the endpoint has additional, more granular error codes, only provide the documentation reference.</td>
 </tr>
 </table>

### REST API Naming and Addressing

<table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">16</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>Encoded slash is not used</td>
 </tr>
  <tr>
   <th style="background-color:#555555">17</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The service interprets values independent of their URL encoding</td>
 </tr>
  <tr>
   <th style="background-color:#555555">18</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>lowerCamelCase is used for names of resources, parameters, and JSON properties</td>
 </tr>
 </table>

### Service Requests and Responses

<table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">19</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>REST API - Request and response payloads are in JSON or binary data format</td>
 </tr>
  <tr>
   <th style="background-color:#555555">20</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>REST API - in JSON format, use relative links, and must not contain schema, hostname, and port. Alternatively, an absolute link can be used, in which case the service must translate the link to the form that goes through the Gateway that is based on the X-Forwarded-* Headers</td>
 </tr>
  <tr>
   <th style="background-color:#555555">21</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>WebSocket (if applicable) - Service URIs contained in WebSocket messages payload are addressed through the API ML Gateway</td>
 </tr>
 <tr>
   <th style="background-color:#555555">22</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>UI (if applicable) - The UI uses relative links and does not contain the schema, hostname, and port. Alternatively an absolute link can be used, in which case the service must translate the link to the form that goes through the Gateway that is based on the X-Forwarded-* Headers</td>
 </tr>
 </table>

### Authentication and Authorization

<table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">23</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Resources are protected by mainframe credentials</td>
 </tr>
  <tr>
   <th style="background-color:#555555">24</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Services accept basic authentication or Single-Sign-On Support as explained in the point 25 (minimum requirement)</td>
 </tr>
  <tr>
   <th style="background-color:#555555">25</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Single-Sign-On Support:  Services accept EITHER Zowe JWT token in the cookie OR support of PassTickets</td>
 </tr>
 </table>

 ### Versioning and Support

<table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">26</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>Service implementation follows the semantic versioning model</td>
 </tr>
  <tr>
   <th style="background-color:#555555">27</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The last two major versions are supported by API services</td>
 </tr>
 </table>

 ### WebSocket Services

<table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">28</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>WebSocket connection creation, all subsequent communication between WebSocket client, and server is routed through the API ML Gateway</td>
 </tr>
  <tr>
   <th style="background-color:#555555">29</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>WebSocket connections are closed by the initiator through API ML Gateway</td>
 </tr>
 </table>

 ### Directory and File Ownership Permissions

<table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">30</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>A conformant application must not modify the contents of the Zowe runtime USS directory and must not change any directory or file permissions or ownership within the Zowe runtime</td>
 </tr>
 <tr>
   <th style="background-color:#555555">31</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>A conformant application must not modify the permissions or ownership of a Zowe instance directory workspace</td>
 </tr>
 </table>

### Lifecycling as a Zowe address space

 <table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th rowspan=4 style="background-color:#555555">32</th>
   <th style="background-color:#555555"></th>
   <th colspan ="3" style="background-color:#AAAAAA">Applicable if LIFECYCLED</th>
   <td>Satisfy the following criteria to lifecycle a service with Zowe:</td>
 </tr>
 <tr>

   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Contains a fully qualified path in the <code>instance.env</code> file for the Zowe workspace which points to the location of a directory containing a <code>start.sh</code> script</td>
 </tr>
 <tr>

   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>Contains a <code>validate.sh</code> script</td>
 </tr>
 <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
  <td>Contains a <code>configure.sh</code> script</td>
 </tr>
 <tr>
<th style="background-color:#555555">33</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
  <td>If the service introduces new variables to the <code>instance.env</code> file, these variables should be prefixed by the provider ID to avoid collisions </td>
 </tr>
 </table>


 ### Support

<table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">34</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The Submitter describes how support is provided. Support details must be clearly documented.</td>
 </tr>

 </table>

#

## Zowe CLI - Zowe v1

### Infrastructure

<table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">1</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The plug-in is constructed on the Imperative CLI Framework</td>
 </tr>
 <tr>
   <th style="background-color:#555555">2</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The plug-in does not run as a standalone CLI (e.g. does not specify a bin field in package.json or other similar techniques to run standalone)</td>
 </tr>

 <tr>
   <th style="background-color:#555555">3</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
  <td>The plug-in commands write to <code>stdout</code> or <code>stderr</code> via Imperative Framework response.console APIs</td>
 </tr>

 </table>

### Installation

<table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">4</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The plug-in is installable with the zowe plugins install command</td>
 </tr>
 <tr>
   <th style="background-color:#555555">5</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The plug-in is installable into the @zowe-v1-lts version of the core Zowe CLI and follows semantic versioning</td>
 </tr>

 <tr>
   <th style="background-color:#555555">6</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The plug-in is uninstallable via the zowe plugins uninstall command</td>
 </tr>

 </table>

 ### Naming

<table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">7</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>If the plug-in introduces a command group name, it must not conflict with existing conformant plug-in group names</td>
 </tr>
 </table>

### Profiles

<table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">8</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>If the plug-in has unique connection details, it introduces a profile that lets users store these details for repeated use</td>
 </tr>
  <tr>
   <th style="background-color:#555555">9</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>Plug-in users are able to override all profile settings via the command line and/or environment variables</td>
 </tr>
 </table>

 ### Support

<table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">10</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The Submitter describes how support is provided. Support details must be clearly documented.</td>
 </tr>
 </table>

#

## Zowe App Framework - Zowe v1

### Packaging

<table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">1</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Every plugin must have a unique ID. The ID format follows java package naming conventions. The Zowe project reserves org.zowe</td>
 </tr>
 <tr>
   <th style="background-color:#555555">2</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Every plugin and each of its services must have a version</td>
 </tr><tr>
   <th style="background-color:#555555">3</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The directory layout adheres to the App filesystem structure</td>
 </tr><tr>
   <th style="background-color:#555555">4</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>Source code is recommended, but not required to adhere to the App filesystem structure for tooling consistency</td>
 </tr>
 </table>

 ### Web UIs All

 <table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">5</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>All Apps must contain an icon image file to represent it, located at code>web/assets/icon.png</code> within the App's package</td>
 </tr>
 </table>

### Web UI iframe

 <table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">6</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Iframe Apps (apps with framework type "iframe") which embed a top-level iframe within them must use the ID "zluxIframe" for that element. <p><b>Example:</b> https://github.com/zowe/api-layer/blob/master/zlux-api-catalog/web/index.html</p> This is required for the app to be a recipient of app to app communication.</td>
 </tr>

 <tr>
   <th style="background-color:#555555">7</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Zowe resources must be accessed via the iframe-adapter located within <code>zlux-app-manager/bootstrap/web</code>. The use of <code>window.parent</code> or <code>window.top</code> to access the ZoweZLUX object is non-permissible.</td>
 </tr>
  <tr>
   <th style="background-color:#555555">8</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Documentation or automated addition of the "iframe" plugin to the Zowe desktop must be performed by executing the <code>zowe-install-app.sh</code> script in the Zowe instance directory</td>
 </tr>
 </table>


### Web UI Non iframe

 <table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">9</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>DOM elements originating from your App are children of the Zowe viewport DOM element, <code>com-rs-mvd-viewport</code> </td>
 </tr>

 <tr>
   <th style="background-color:#555555">10</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Network requests to the Zowe App Server must never be done without the use of the URI Broker. This ensures compatibility with future versions of Zowe if URLs change.</td>
 </tr>
  <tr>
   <th style="background-color:#555555">11</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>Access to resources outside the App Server should be made through the URI Broker whenever possible</td>
 </tr>
   <tr>
   <th style="background-color:#555555">12</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Apps must not pollute the global namespace with regards Javascript, HTML, and CSS</td>
 </tr>
   <tr>
   <th style="background-color:#555555">13</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>When using a library present in the Zowe App Framework core, you must depend on the same version </td>
 </tr>
   <tr>
   <th style="background-color:#555555">14</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Web apps should extend the framework's default build scripts for webpack and typescript.</td>
 </tr>
 </table>

### UI Design

 <table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">15</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>Apps should follow the UI Design guidelines at <a href=https://github.com/zowe/zlc/blob/master/process/UI_GUIDELINES.md>https://github.com/zowe/zlc/blob/master/process/UI_GUIDELINES.md</a></td>
 </tr>
 </table>

 ### Localization and Internationalization l10n and l18n

 <table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">16</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>If your software supports multiple languages, the active language to be used for string selection must be retrieved using ZoweZLUX.globalization.getLanguage(), which determines language by multiple factors</td>
 </tr>
  <tr>
   <th style="background-color:#555555">17</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>No strings visible in a UI should be hard-coded. Resource strings must be used in accordance with one of the existing internationalization support mechanisms.</td>
 </tr>
 </table>

### App Server

 <table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">18</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Data services should be written such that all synchronous and asynchronous errors are caught. Utilize try-catch and check the existence of error objects from asynchronous calls. Uncaught exceptions affect server responsiveness and disrupts clients.</td>
 </tr>
</table>

### Documentation

 <table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">19</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Every HTTP API must be documented in swagger 2.0. The swagger document must be stored in doc/swagger.</td>
 </tr>
 <tr>
   <th style="background-color:#555555">20</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>In addition, we recommend documentation about the format of any Websocket APIs, to be included in the doc</td>
 </tr>
</table>


### Logging

 <table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">21</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>An Apps non-Iframe web components, or App Framework dataservices (eg Javascript and Typescript) must log only through the "zlux" logger</td>
 </tr>
 <tr>
   <th style="background-color:#555555">22</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>ZSS services log only through the Zowe ZSS Logger</td>
 </tr>
  <tr>
   <th style="background-color:#555555">23</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Passwords must never be logged</td>
 </tr>
  <tr>
   <th style="background-color:#555555">24</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>Error reporting should follow the standard tooling</td>
 </tr>
</table>

### Encoding

 <table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">25</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>Application Framework plugins serving web content through App Server or doing file I/O through an App Server dataservice should tag these files on z/OS according to their content type</td>
 </tr>
 <tr>
   <th style="background-color:#555555">26</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>Testing Apps via the install-app script is advisable to enable end users to utilize Zowe plugin management tooling</td>
 </tr>
 </table>

 ### Storage

 <table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">27</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>User preferences, if applicable to a plug-in, must be stored through the configuration data service, unless the software needs pre-existing storage structures such as DB2 </td>
 </tr>
 <tr>
   <th style="background-color:#555555">28</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>For other plugin storage needs, storing data outside of the configuration dataservice is permitted only within <code>$INSTANCE_DIR/workspace/app-server</code> or <code>$INSTANCE_DIR/workspace/app-server/pluginStatic</code> with a top-level folder equal to their plugin ID. Plugins must not store information anywhere else in any Zowe directories such as <code>$INSTANCE_DIR</code> or <code>$ROOT_DIR</code> in order to prevent conflict with future Zowe versions and other plugins </td>
 </tr>
  <tr>
   <th style="background-color:#555555">29</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>It is advisable for the storage of user preferences to use environment variables for locating directories. The use of the instance directory environment variable is not required, however we recommend the use of this variable to subvert the use of hard-coded paths</td>
 </tr>
 </table>

 ### Directory and File Ownership Permissions

 <table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">30</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>A conformant application must not modify the contents of the Zowe root directory <code>$ROOT_DIR</code> and must not change any directory or file permissions or ownership </td>
 </tr>
 <tr>
   <th style="background-color:#555555">31</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>A conformant application must not modify the permissions or ownership of a Zowe instance directory workspace</td>
 </tr>
 </table>

 ### Lifecycling as a Zowe address space

 <table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th rowspan=4 style="background-color:#555555">32</th>
   <th style="background-color:#555555"></th>
   <th colspan ="3" style="background-color:#AAAAAA">Applicable if LIFECYCLED</th>
   <td>If the app framework plugin requires services that do not originate from Zowe, but require the same lifecycle as Zowe, satisfy the following criteria to lifecycle them with Zowe:</td>
 </tr>
 <tr>

   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The service should provide a fully qualified path in the <code>instance.env</code> file for the Zowe workspace which points to the location of a directory containing a <code>start.sh</code> script</td>
 </tr>
 <tr>

   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>Contain a <code>validate.sh</code> script</td>
 </tr>
 <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
  <td>Contain a <code>configure.sh</code> script</td>
 </tr>
 <tr>
<th style="background-color:#555555">33</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
  <td>If the service introduces new variables to the <code>instance.env</code> file, these variablesshould be prefixed by the provider ID to avoid collisions </td>
 </tr>
 </table>


 ### Support

 <table rules="all">
 <thead>
  <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">34</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The Submitter describes how support is provided. Support details must be clearly documented</td>
</table>

#

## Zowe Explorer for VS Code - Zowe v1

Throughout the this Zowe Explorer for VS Code section you will find the following terminology being used:

- _Extender_: The organization or developer producing an extension for Zowe Explorer for VS Code.
- _Zowe Explorer for VS Code Extension_: An installable piece of software that provides new functionality to Zowe Explorer for VS Code or uses/calls services provided by Zowe Explorer for VS Code. Also simply referred to here as an "extension", this can be a VS Code extension as well as a Zowe CLI Plugin or an independent piece of software. The conformance criteria below call out conformance requirements for three common types of Zowe Explorer for VS Code extensions, but it is possible that more kinds of extensions can be created. If such new extension kinds surface, then Zowe Explorer for VS Code APIs and this document can be expanded to support them in the future.
- _Zowe Explorer for VS Code VS Code extension_: Refers to a Zowe Explorer for VS Code extension that is a VS Code extension that is installed in addition to Zowe Explorer for VS Code ad that has a VS Code extension dependency to Zowe Explorer for VS Code.
- _Zowe SDKs_ are [SDKs published by the Zowe project](https://docs.zowe.org/stable/user-guide/sdks-using) that provides various APIs for writing Zowe-based capabilities in general.

### General Extension

General conformance criteria for all extensions that add new capabilities to Zowe Explorer for VS Code.

<table rules="all">
 <thead>
 <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">1</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td><b>Naming:</b> If the extension uses the word "Zowe" in its name, it abides by The Linux Foundation <a href="https://www.linuxfoundation.org/trademark-usage/">Trademark Usage Guidelines</a> and <a href="https://www.openmainframeproject.org/branding-guidelines">Branding Guidelines</a> to ensure the word Zowe is used in a way intended by the Zowe community.</td>
 </tr>

 <tr>
   <th style="background-color:#555555">2</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td><b>No Zowe CLI plugin installation requirement: </b> If the extender makes use of a Zowe CLI profile other than the Zowe Explorer for VS Code default `zosmf` then the extension must not make any assumptions that a matching Zowe CLI plugin has been installed in the Zowe Explorer for VS Code user's environment.</td>
 </tr>

 <tr>
   <th style="background-color:#555555">3</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td><b>Publication tag:</b> If the extension is published in a public catalog or marketplace such as Npmjs, Open-VSX, or VS Code Marketplace, it uses the tag or keyword "Zowe" so it can be found when searching for Zowe and be listed with other Zowe offerings.</td>
 </tr>

 <tr>
   <th style="background-color:#555555">4</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td><b>Support:</b> Extension has documentation with instructions on how to report problems that are related to the extension and not Zowe Explorer for VS Code. It needs to explain how users can determine if a problem is related to the extension or Zowe Explorer for VS Code.</td>
 </tr>

 <tr>
   <th style="background-color:#555555">5</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td><b>User settings consistency:</b> Extender provides a consistent user settings experience. For VS Code extensions, extender follows the recommended naming convention for configuration settings as described in VS Code's <a href="https://code.visualstudio.com/api/references/contribution-points#contributes.configuration">configuration contribution documentation</a>, and avoids starting setting names with the prefix `zowe.`, which is reserved for Zowe Explorer for VS Code.</td>
 </tr>

 <tr>
   <th style="background-color:#555555">6</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td><b>Error message consistency:</b> Extension follows the recommended error message format indicated in the Zowe Explorer for VS Code extensibility documentation to provide a consistent user experience with Zowe Explorer for VS Code.</td>
 </tr>

 <tr>
   <th style="background-color:#555555">7</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td><b>Zowe SDK usage:</b> Extension utilizes the available Zowe SDKs that standardize z/OS interactions as well as other common capabilities that are used by many other Zowe extensions and tools unless the extension's goal is to provide a new implementation with clearly stated goals.</td>
 </tr>

 <tr>
   <th style="background-color:#555555">8</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td><b>Sharing of profiles with Zowe CLI:</b> Extensions that utilize Zowe CLI profiles must share the created profile instances between Zowe CLI and the Zowe Explorer for VS Code extension that utilize them.</td>
 </tr>
 <tr>
   <th style="background-color:#555555" rowspan=5>9</th>
   <th style="background-color:#555555"></th>
   <th style="background-color:#AAAAAA" colspan=2>Mark (a) or (b) or (c)</th>
   <th style="background-color:#AAAAAA"></th>
   <td style="text-align:center">Extension uses the extensibility APIs provided by Zowe Explorer for VS Code. Supported methods include:<p style="color:red">(Please select all that apply _a_, _b_, or _c_)</td>
 </tr>
 <tr>
   <th style="background-color:#555555"></th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
  <td>a. Extension Accessing Profiles</td>
 </tr>
 <tr>
   <th style="background-color:#555555"></th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
  <td>b. Data Provider Extension</td>
 </tr>
 <tr>
   <th style="background-color:#555555"></th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
  <td>c. Extension Adding Menus</td>
 </tr>
</table>

### Extension Accessing Profiles

Criteria for VS Code extensions that want to access the same Zowe CLI profiles that Zowe Explorer for VS Code uses.

<table rules="all">
 <thead>
 <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">10</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td><b>VS Code extension dependency:</b> Extension declares Zowe Explorer for VS Code as a VS Code extension dependency by including an `extensionDependencies` entry for Zowe Explorer for VS Code in its package.json file.</td>
 </tr>

  <tr>
   <th style="background-color:#555555">11</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td><b>Zowe Extender access:</b> Extension accesses the shared Zowe Explorer for VS Code profiles cache via `ZoweExplorerApi.IApiRegisterClient.getExplorerExtenderApi()` API as documented in the Zowe Explorer for VS Code extensibility documentation.</td>
 </tr>

  <tr>
   <th style="background-color:#555555">12</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td><b>Added Profile Type initialization:</b> If the extension has a dependency on a new Zowe CLI profile type other than the Zowe Explorer for VS Code default `zosmf`, it is calling the `ZoweExplorerApi.IApiRegisterClient.getExplorerExtenderApi().initialize(profileTypeName)` to ensure that the profile type is supported and managed by the extension without a Zowe CLI plugin installed.</td>
 </tr>
</table>

### Data Provider Extension

Criteria for VS Code extensions that extend the Zowe Explorer for VS Code MVS, USS, or JES tree views to use alternative z/OS interaction protocols such as FTP or a REST API.

<table rules="all">
 <thead>
 <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">13</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td><b>New Zowe CLI profile type:</b> Extension registers its new API instances with a new profile type name for the different Zowe Explorer for VS Code views via the `ZoweExplorerApi.IApiRegisterClient.register{Mvs|Uss|Jes}Api(profileTypeName)` call as indicated from the Zowe Explorer for VS Code extensibility documentation</td>
 </tr>

 <tr>
   <th style="background-color:#555555">14</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td><b>Matching Zowe CLI Plugin:</b> Provide a Zowe CLI Plugin for the data provider's new profile type that implements the core capabilities required for the new protocol that users can then also use to interact with the protocol outside of the Zowe Explorer for VS Code extension using Zowe CLI commands.</td>
 </tr>

 <tr>
   <th style="background-color:#555555">15</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td><b>Data provider API implementation:</b> Extension fully implements and registers to at least one of the three Zowe Explorer for VS Code interfaces or alternatively throw exceptions that provide meaningful error messages to the end-user in the 'Error.message' property that will be displayed in a dialog.</td>
 </tr>

 <tr>
   <th style="background-color:#555555">16</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td><b>API test suite implementation:</b>  If the extension implements a Zowe Explorer for VS Code API data provider interface, it should implement a test suite that calls each of the implemented API methods.</td>
 </tr>

 <tr>
   <th style="background-color:#555555">17</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td><b>Base Profile and Tokens:</b> Extension supports base profiles and tokens (For more information, click here)</td>
 </tr>

 <tr>
   <th style="background-color:#555555">18</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td><b>Team Configuration File:</b> Extension supports the Zowe CLI 7 team configuration file format as an alternative to the Zowe CLI 6 profiles file format.</td>
 </tr>

 <tr>
   <th style="background-color:#555555">19</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td><b>Secure Credential Store:</b> If the extension supports Zowe CLI's Secure Credential store, it calls the Zowe Explorer for VS Code-provided method for initialization at startup.</td>
 </tr>
</table>

### Extension Adding Menus

Criteria for VS Code extensions adding menu and commands to VS Code that utilize Zowe Explorer for VS Code data or extend Zowe Explorer for VS Code capabilities.

<table rules="all">
 <thead>
 <th style=background-color:#5555AA>Item </th>
 <th style=background-color:#5555AA>Ver </th>
 <th style=background-color:#5555AA>Required </th>
 <th style=background-color:#5555AA>Best Practice </th>
 <th style=background-color:#5555AA>Conformant </th>
 <th style=background-color:#5555AA>Criteria </th>
 </thead>

 <tr>
   <th style="background-color:#555555">20</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td><b>Command operations: </b> If the extension is adding new commands to Zowe Explorer for VS Code's tree views, the commands must not replace any existing Zowe Explorer for VS Code commands.</td>
 </tr>

  <tr>
   <th style="background-color:#555555">21</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td><b>Command categories: </b>  If the extension adds to <code>contributes.commands</code> in <code>package.json</code>, the value assigned to the <code>category</code> property contains the extension name and it cannot be "Zowe Explorer for VS Code".</td>
 </tr>

  <tr>
   <th style="background-color:#555555">22</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td><b>Context menu groups: </b> If contributing commands to Zowe Explorer for VS Code's context menus, the extension follows the Zowe Explorer for VS Code extensibility documentation and adds them in new context menu groups that are located below Zowe Explorer for VS Code's existing context menu groups in the user interface.</td>
 </tr>

  <tr>
   <th style="background-color:#555555">23</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td><b>Menu Names:</b> If the extension is adding new commands and context menu entries to the Zowe Explorer for VS Code tree view nodes, the new command name is consistent with the terminology and naming conventions of the existing Zowe Explorer for VS Code menu entries.</td>
 </tr>

 <tr>
   <th style="background-color:#555555">24</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td><b>Context menu items: </b> If contributing commands to Zowe Explorer for VS Code's views (such as Data Sets, USS, or Jobs), the extension should only add them to the view's right-click context menus.</td>
 </tr>
</table>

