# Zowe Conformance Test Evaluation Guide

The Zowe Conformance Test Evaluation Guide is a set of self-certify and self-service tests to help the developer community integrate and extend specific technology into the Zowe framework. 

Below are the requirements for the available conformance programs. Items marked **(required)** are required for achieving conformance in a given program. Items marked **(best practice)** are considered a best practice for conformant applications.

These Zowe Conformant criteria are applicable to the lastest Zowe v1 LTS Release.

- [Zowe API Mediation Layer - Zowe V1](#zowe-api-mediation-layer---zowe-v1)
  - [Application Service](#application-service)
  - [API Documentation](#api-documentation)
  - [API Naming and Addressing](#api-naming-and-addressing)
  - [Service Requests and Responses](#service-requests-and-responses)
  - [Authentication and Authorization](#authentication-and-authoriation)
  - [Versioning and Support](#versioning-and-support)
  - [UI](#ui)
  - [WebSocket Services](#websocket-services)
  - [Lifecycling](#lifecycling)
  - [Directory and File Ownership Permissions](#directory-and-file-ownership-permissions)
  - [Support](#support)
- [Zowe CLI - Zowe v1](#zowe-cli---zowe-v1)
  - [Infrastructure](#infrastructure)
  - [Installation](#installation)
  - [Naming](#naming)
  - [Profiles](#profiles)
  - [Support](#support)


## Zowe API Mediation layer - Zowe V1

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
   <td>An application service provides at least one service of UI register with discovery services</td>
 
 </tr>
 <tr>
   <th style="background-color:#555555" rowspan=3>2</th>
   <th style="background-color:#555555"></th>
   <th style="background-color:#AAAAAA" colspan=2>Mark (a) or (b)</th>
   <th style="background-color:#AAAAAA"></th>
   <td style="text-align:center"><b>A service must be reigstered using one of the following methods</b><p style="color:red"> [please mark which one applies (a) or (b)</td>
  
 </tr>
  <tr>
   <th style="background-color:#555555">v1</th>
   <td style="background-color:#AAAAAA"></th>
   <td style="background-color:#AAAAAA" >x</th>
   <td></th>
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
   <td>The service must provide a daefault service ID that is prefixed by the provider name (for example: 'acme','xyzcorp','bar')</td>
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
   <td>The service ID must be written in lower case, contain no symbols, and is limited to 64 characters</td>

 <tr>
   <th style="background-color:#555555">6</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>The API ID must follow the same rules for Java packages. The example of the API ID:zowe.apiml.apicatalog</td>

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
   <th style="background-color:#555555" rowspan=8>8</th>
   <th style="background-color:#555555"></th>
   <th style="background-color:#AAAAAA" colspan=2>Versioned</th>
   <th style="background-color:#AAAAAA"></th>
   <td style="text-align:center"><b>For versioned APIs, service URL must contain a service version before the service ID in the following formats:</b><p style="color:red">[mark just one section - Versioned or Non-Versioned]</td>

 </tr>
  <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td>  - api/v1/{serviceId} reserved for REST APIs</td>
 </tr>
  <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td> - ui/v1/{serviceId} reserved for Uis</td>
 </tr>
   <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td> - ui/v1/{serviceId} reserved for Uis</td>
 </tr>
<tr>
   <th style="background-color:#555555"></th>
   <th style="background-color:#AAAAAA" colspan=2>Non-Versioned</th>
   <th style="background-color:#AAAAAA"></th>
   <td>For non-versioned APIs or APIs versioned differently (e.g. z/OSMF), use the following formats</td>
 </tr>
  <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td>  - api/{serviceId} reserved for REST APIs</td>
 </tr>
  <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td>  - ui/{serviceId} reserved for UIs</td>
 </tr>
   <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td>  - ws/{serviceId} reserved for WebSockets</td>
 </tr>

 <tr>
   <th style="background-color:#555555" rowspan=4>9</th>
   <th style="background-color:#555555"></th>
   <th style="background-color:#AAAAAA" colspan=2>Mark (a) or (b)</th>
   <th style="background-color:#AAAAAA"></th>
   <td style="text-align:center"><b>The registration of the serice must not obe done by modifying the Zowe runtime directory api-defs folder. Supported methods include:</b><p style="color:red">[please mark which one applies (a) or (b) or (c)]:</td>
 </tr>
  <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td>a. adding the static API definition YAML file path to instance.env file for the Zowe workspace</td>
 </tr>
  <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td>b. copying the static API definition YAML file to the instance directory workspace api-definnitions diretory</td>
 </tr>
   <tr>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA" ></th>
   <th></th>
   <td>c. adding the path of a launch component to the instance.env file for the Zowe workspace</td>
  </tr>

</table>

### API Documentation

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
   <td>Every method of each REST endpoint is documented</td>
 </tr>
 <tr>
   <th style="background-color:#555555">13</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Every method of each REST endpoint is demonstrated by example</td>
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
   <td>Every HTTP error codoe must be documented. IF endpoint has additional more granulator error codes just the documentation reference can be provided for these</td>
 </tr>
 </table>

### API Naming and Addressing

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
   <td>API - Request and response payloads are in JSON or binary data format</td>
 </tr>
  <tr>
   <th style="background-color:#555555">20</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>API - in JSON format, linkes are relative, and must not contain the schema, hostname, and port</td>
 </tr>
  <tr>
   <th style="background-color:#555555">21</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>WebSocket - Service URIs contained in WebSocket messages payload are addressed through the API ML Gateway</td>
 </tr>
 <tr>
   <th style="background-color:#555555">22</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>UI - UI uses relative links and does not contain the schema, hostname, and port</td>
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
   <td>Services accept basic authentication (minimum requirement)</td>
 </tr>
  <tr>
   <th style="background-color:#555555">25</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Single-Sign-On Support:  Services accept EITHER Zowe JWT token in the cookie OR support PassTickets</td>
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
   <td>Last two major versions are supported by API services</td>
 </tr>
 </table>

### UI

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
   <td>UI uses only relative URLs</td>
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
   <th style="background-color:#555555">29</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>WebSocket connection creation, all subsequent communication between WebSocket client, and server is routed through the API ML Gateway</td>
 </tr>
  <tr>
   <th style="background-color:#555555">30</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>WebSocket connections are closed by the initiator through API ML Gateway</td>
 </tr>
 </table>


### Lifecycling

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
   <th style="background-color:#555555">31</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>Running as a Zowe address space</td>
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
   <th style="background-color:#555555">32</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>A conformant application must not modify the contents of the Zowe runtime USS directory and it must not change any directory or file permissions or ownership within the Zowe runtime</td>
 </tr>
 <tr>
   <th style="background-color:#555555">33</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>A conformant application must not modify the permissions or ownership of a Zowe instance directory workspace</td>
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
   <td>Submitter describes how Support is provided and Support details are clearly documented</td>
 </tr>

 </table>


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
   <td>Plug-in is constructed on the Imperative CLI Framework</td>
 </tr>
 <tr>
   <th style="background-color:#555555">2</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Plug-in should not run as a standalone CLI (e.g. does not specify a bin field in package.json or other similar techniques to run standalone)</td>
 </tr>

 <tr>
   <th style="background-color:#555555">3</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Plug-in commands write to stdout or stderr via Imperative Framework response.console APIs</td>
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
   <td>Plug-in is installable with the zowe plugins install command</td>
 </tr>
 <tr>
   <th style="background-color:#555555">5</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Plug-in is installable into the @zowe-v1-lts version of the core Zowe CLI and follows semantic versioning</td>
 </tr>

 <tr>
   <th style="background-color:#555555">6</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Plug-in is uninstallable via the zowe plugins uninstall command</td>
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
   <td>If the plug-in introduces a command group name, it does not conflict with existing conformant plug-in group names</td>
 </tr>

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
   <td>Submitter describes how Support is provided and Support details are clearly documented</td>
 </tr>
 </table>

## Zowe App Framework -- Zowe v1

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
   <td>Every plugin must have a unique ID.  The ID format follows java package naming conventions.  The Zowe project reserves org.zowe</td>
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
   <td>Directory layout adheres to the App filesystem structure</td>
 </tr><tr>
   <th style="background-color:#555555">4</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>Source code is also recommended, but not required to adhere to the App filesystem structure for tooling consistency</td>
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
   <td>All Apps must contain an icon image file to represent it, located at web/assets/icon.png within the App's package</td>
 </tr>
 </table>

### Web UI iFrame

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
   <td>IFrame Apps (apps with framework type "iframe") which embed a top-level iframe within (example: https://github.com/zowe/api-layer/blob/master/zlux-api-catalog/web/index.html) must use the ID "zluxIframe" for that element. This is required for the app to be a recipient of app to app communication.</td>
 </tr>

 <tr>
   <th style="background-color:#555555">7</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Zowe resources must be accessed via the iframe-adapter located within zlux-app-manager/bootstrap/web.  Use of window.parent or window.top to access the ZoweZLUX object is non-permissible.</td>
 </tr>
  <tr>
   <th style="background-color:#555555">8</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Documentation or automated addition of the "iframe" plugin to the Zowe desktop must be performed by executing the script 'zowe-install-app.sh' script in the Zowe instance directory</td>
 </tr>
 </table>


### Web UI Non0iframe

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
   <td>DOM elements originating from your App should always be a child of the Zowe viewport DOM element, "com-rs-mvd-viewport" </td>
 </tr>

 <tr>
   <th style="background-color:#555555">10</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Network requests to the Zowe App Server must never be done without the use of the URI Broker</td>
 </tr>
  <tr>
   <th style="background-color:#555555">11</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>Access to resources outside the App Server should also be made through the URI Broker whenever possible</td>
 </tr>
   <tr>
   <th style="background-color:#555555">12</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA">x</th>
   <th style="background-color:#AAAAAA"></th>
   <th></th>
   <td>Access to resources outside the App Server should also be made through the URI Broker whenever possible</td>
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
   <td>Apps should follow the UI Design guidelines at https://github.com/zowe/zlc/blob/master/process/UI_GUIDELINES.md</td>
 </tr>
 </table>

 ### Localization and Internationalization (l10n and l18n)

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
   <td>The active language to be used for string selection must be retrieved using ZoweZLUX.globalization.getLanguage(), which determines language by multiple factors</td>
 </tr>
  <tr>
   <th style="background-color:#555555">17</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>No strings visible in a UI should be hard-coded, rather resource strings must be used in accordance with one of the existing internationalization support mechanisms</td>
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
   <td>Data services should be written such that all synchronous and asynchronous errors are caught. Utilize try-catch and check the existence of error objects from asynchronous calls. Uncaught exceptions effect server responsiveness and disrupt clients</td>
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
   <td>Every HTTP API must be documented in swagger 2.0. The swagger document must be stored in doc/swagger</td>
 </tr>
 <tr>
   <th style="background-color:#555555">20</th>
   <th style="background-color:#555555">v1</th>
   <th style="background-color:#AAAAAA"></th>
   <th style="background-color:#AAAAAA">x</th>
   <th></th>
   <td>In addition, it is recommended to have documentation about the format of any Websocket APIs, to be placed within doc</td>
 </tr>
</table>



1.  **Packaging**

    a.  Every plugin must have a unique ID. The ID format follows java package naming conventions. The Zowe project reserves org.zowe. **(required)**

    b.  Every plugin and each of its services must have a version. **(required)**

    c.  Directory layout adheres to the App filesystem structure. **(required)**

    d.  Source code layout is recommended adheres to the App filesystem structure for tooling consistency. **(best practice)**

2.  **Web UIs ALL**

    a.  All Apps must contain an icon image file to represent it, located at web/assets/icon.png within the App\'s package. **(required)**

3.  **Web UI IFrame**

    a.  IFrame Apps (apps with framework type \"iframe\") which embed a top-level iframe within (example: <https://github.com/zowe/api-layer/blob/master/zlux-api-catalog/web/index.html>) must use the ID \"zluxIframe\" for that element. This is required for the app to be a recipient of app to app communication. **(required)**

    b.  Zowe resources must be accessed via the iframe-adapter located within zlux-app-manager/bootstrap/web. Use of window.parent or window.top to access the ZoweZLUX object is non-permissible. **(required)**

    c.  Documentation or automated addition of the "iframe" plugin to the Zowe desktop must be performed by executing the script 'zowe-install-app.sh' script in the Zowe instance directory. **(required)**

4.  **Web UI Non-IFrame**

    a.  DOM elements originating from your App should always be a child of the Zowe viewport DOM element, \"com-rs-mvd-viewport\". **(required)**

    b.  Network requests to the Zowe App Server must never be done without the use of the URI Broker. **(required)**

    c.  Access to resources outside the App Server should also be made through the URI Broker whenever possible. **(best practice)**

    d.  Apps must not pollute the global namespace with regards Javascript, HTML, and CSS. **(required)**

    e.  When using a library present in the Zowe App Framework core, you must depend on the same version. **(required)**

    f.  Web apps should extend the framework\'s default build scripts for webpack and typescript. **(best practice)**

5.  **UI Design**

    a.  Apps should follow the UI Design guidelines at <https://github.com/zowe/zlc/blob/master/process/UI_GUIDELINES.md> **(best practice)**

6.  **Localization and Internationalization (I10n and I18n)**

    a.  The active language to be used for string selection must be retrieved using ZoweZLUX.globalization.getLanguage(), which determines language by multiple factors. **(required)**

    b.  No strings visible in a UI should be hard-coded, rather resource strings must be used in accordance with one of the existing internationalization support mechanisms. **(best practice)**

7.  **App Server**

    a.  Data services should be written such that all synchronous and asynchronous errors are caught. Utilize try-catch and check the existence of error objects from asynchronous calls. Uncaught exceptions effect server responsiveness and disrupt clients. **(required)**

8.  **Documentation**

    a.  Every HTTP API must be documented in swagger 2.0. The swagger document must be stored in doc/swagger. **(required)**

    b.  In addition, it is recommended to have documentation about the format of any Websocket APIs, to be placed within doc. **(best practice)**

9.  **Logging**

    a.  An Apps non-IFrame web components, or App Framework dataservices (eg Javascript and Typescript) must log only through the \"zlux\" logger. **(required)**

    b.  ZSS services log only through the Zowe ZSS Logger. **(required)**

    c.  Passwords must never be logged. **(required)**

    d.  Error reporting should follow the standard tooling. **(best practice)**

10. **Storage**

    a.  User preferences, if applicable to a plugin, must be stored through the configuration data service. **(required)**

    b.  For other plugin storage needs, storing data outside of the configuration dataservice is permitted only within $INSTANCE_DIR/workspace/app-server or $INSTANCE_DIR/workspace/app-server/pluginStatic with a top-level folder equal to their plugin ID. Plugins must not store information anywhere else in any Zowe directories such as $INSTANCE_DIR or $ROOT_DIR in order to prevent conflict with future Zowe versions and other plugins. **(required)**

    c.  It is advisable for the storage of user preferences to use environment variables for locating directories. Use of the instance directory environment variable is not required, but should be considered to subvert the use of hard-coded paths. **(best practice)**

11. **Directory and File Ownership Permissions**

    a.  A conformant application must not modify the contents of the Zowe runtime USS directory and it must not change any directory or file permissions or ownership. **(required)**

    b.  A conformant application must not modify the permissions or ownership of a Zowe instance directory workspace. **(best practice)**

12. **Lifecycling as a Zowe address space**

    a.  If the service should be lifecycled by Zowe then it should provide \
             - a fully qualified path in the instance. env file for the Zowe workspace which points to the location of a directory containing a start.sh script. **(required)**\
             - a validate.sh script. **(best practice)**\
             - a configure.sh script. **(best practice)**

    b.  If the service introduces new variables to the instance. env file, these should be prefixed by the provider ID to avoid collisions. **(required)**

13. **Support**

    a.  Submitter describes how Support is provided and Support details are clearly documented
