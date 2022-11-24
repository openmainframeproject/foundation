# Zowe Conformance Test Evaluation Guide

The Zowe Conformance Test Evaluation Guide is a set of self-certifying and self-service tests to help the development community integrate and extend specific technology into the Zowe framework. 

This guide describes the requirements of the four available conformance programs. Items marked **(required)** are required for an application to be conformant. Items marked **(best practice)** are considered best practices for conformant applications.

These Zowe Conformance criteria are applicable to the lastest Zowe LTS Release.

- [Zowe Conformance Test Evaluation Guide](#zowe-conformance-test-evaluation-guide)
  - [Zowe API Mediation Layer](#zowe-api-mediation-layer)
    - [Application Service](#application-service)
    - [REST API Documentation](#rest-api-documentation)
    - [REST API Naming and Addressing](#rest-api-naming-and-addressing)
    - [Service Requests and Responses](#service-requests-and-responses)
    - [Authentication and Authorization](#authentication-and-authorization)
    - [Versioning and Support](#versioning-and-support)
    - [WebSocket Services](#websocket-services)
    - [Directory and File Ownership Permissions](#directory-and-file-ownership-permissions)
    - [Packaging](#packaging)
    - [Support](#support)
  - [Zowe CLI](#zowe-cli)
    - [Infrastructure](#infrastructure)
    - [Installation](#installation)
    - [Naming](#naming)
    - [Profiles](#profiles)
    - [Support](#support-1)
    - [Documentation](#documentation)
  - [Zowe Application Framework](#zowe-application-framework)
    - [Packaging](#packaging-1)
    - [Packaging Format and Manifest](#packaging-format-and-manifest)
    - [Web UIs All](#web-uis-all)
    - [Web UI IFrame](#web-ui-iframe)
    - [Web UI Non-IFrame](#web-ui-non-iframe)
    - [UI Design](#ui-design)
    - [Localization and Internationalization (l10n and l18n)](#localization-and-internationalization-l10n-and-l18n)
    - [App Server](#app-server)
    - [Documentation](#documentation-1)
    - [Logging](#logging)
    - [Encoding](#encoding)
    - [Storage](#storage)
    - [Directory and File Ownership Permissions](#directory-and-file-ownership-permissions-1)
    - [Lifecycling as a Zowe address space](#lifecycling-as-a-zowe-address-space)
    - [Support](#support-2)
  - [Zowe Explorer for Visual Studio Code](#zowe-explorer-for-visual-studio-code)
    - [General Extension](#general-extension)
    - [[a] Extension Interacts with mainframe assets delivered by Zowe Explorer](#a-extension-interacts-with-mainframe-assets-delivered-by-zowe-explorer)
    - [[b] Extension Accessing Profiles](#b-extension-accessing-profiles)
    - [[c] Extension Serves as a Data Provider](#c-extension-serves-as-a-data-provider)
    - [[d] Extension Adding Menus](#d-extension-adding-menus)

## Zowe API Mediation Layer

### Application Service 

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">1</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >The product or applications that extends Zowe API ML must provide at least one API service registered with the Zowe API ML Discovery Service</td>
</tr>
<tr>
<td rowspan="3" style="background-color: #555555">2</td>
<td style="background-color: #555555">&nbsp;</td>
<td colspan="3" style="background-color: #AAAAAA">Mark (a) or (b)</td>
<td style="background-color: #AAAAAA">A service must be registered using one of the following methods<br />&nbsp; [please mark which one applies (a) or (b)]:</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >a.&nbsp; Dynamic Registration</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >b . Static Definition&nbsp;</td>
</tr>
<tr>
<td style="background-color: #555555">3</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >The service must provide a default service ID that is prefixed by the organization/provider name.<br />Examples of compliant service IDs:<br />zowemonitoring, bcmjclcheck, ibmims, rocketterasam<br />Examples of non-compliant service IDs:<br />jclcheck, myims, mydb2<br />Note:&nbsp;The service ID is part of the URL</td>
</tr>
<tr>
<td style="background-color: #555555">4</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >The service ID must be configurable externally after deployment</td>
</tr>
<tr>
<td style="background-color: #555555">5</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >The service ID must be written in lower case, contain no symbols, and is limited to 64 characters</td>
</tr>
<tr>
<td style="background-color: #555555">6</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >Services must provide API ID to provide grouping of APIs provided by multiple services. The API ID is for example used for Automated CLI Client Configuration. The API ID must be prefixed by the organization/provider name. Example of the API ID: zowe.apiml.apicatalog <br />Note: API ID isn't part of the URL</td>
</tr>
<tr>
<td style="background-color: #555555">7</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >The published service URL must follow the gateway URL conventions</td>
</tr>
<tr>
<td style="background-color: #555555" rowspan="9">8</td>
<td style="background-color: #555555"></td>
<td colspan="2" style="background-color: #AAAAAA">Versioned</td>
<td style="background-color: #AAAAAA"></td>
<td  style="background-color: #AAAAAA">For versioned APIs, service URLs must contain a service ID in the first place in the path, before the service version (all formats). Example formats: (Mark only one section - Versioned or Non-Versioned)</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >- {serviceId}/api/v1 reserved for REST APIs</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >- {serviceId}/ui/v1 reserved for UIs</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >- {serviceId}/ws/v1 reserved for WebSockets</td>
</tr>
<tr>
<td style="background-color: #555555">&nbsp;</td>
<td colspan="2" style="background-color: #AAAAAA">Non-Versioned</td>
<td style="background-color: #AAAAAA"></td>
<td  style="background-color: #AAAAAA">For non-versioned APIs or APIs versioned differently (e.g. z/OSMF), use the following formats:&nbsp;</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >- {serviceId}/api reserved for REST APIs</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >- {serviceId}/ui reserved for UIs</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >- {serviceId}/ws reserved for WebSockets</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >- {serviceId}/graphql reserved for GraphQL APIs</td>
</tr>
<tr>
<td rowspan="4" style="background-color: #555555">9</td>
<td style="background-color: #555555">&nbsp;</td>
<td colspan="3" style="background-color: #AAAAAA">Mark<br />&nbsp;(a), (b) or (c)</td>
<td style="background-color: #AAAAAA">Registration of the service must be performed via one of the supported methods: (Mark which one applies _a_, _b_, _c_)</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >a. Adding the static API definition YAML file path to&nbsp;zowe.yaml</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >b. Copying the static API definition YAML file to the workspace api-definitions directory</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >c. Dynamic registration of an application</td>
</tr>
</tbody>
</table>

### REST API Documentation

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">10</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >Documentation is Swagger/Open API 2.0/Open API 3.0 compliant</td>
</tr>
<tr>
<td style="background-color: #555555">11</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >Every public resource is documented with a description of each end-point</td>
</tr>
<tr>
<td style="background-color: #555555">12</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >Every method of each public REST endpoint is documented</td>
</tr>
<tr>
<td style="background-color: #555555">13</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >Every method of each public REST endpoint is demonstrated by example. The examples are part of the documentation.</td>
</tr>
<tr>
<td style="background-color: #555555">14</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >Every parameter (headers, query parameters, payload, cookies, status codes etc.) is documented with definitions of all possible values and their associated meanings</td>
</tr>
<tr>
<td style="background-color: #555555">15</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >Every HTTP error code must be documented. If the endpoint has additional and more granular error codes only provide the documentation reference.</td>
</tr>
<tr>
<td style="background-color: #555555">16</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>Service SHOULD provide the code snippets to be shown to the users as explained in https://docs.zowe.org/stable/extend/extend-apiml/onboard-plain-java-enabler/#api-info</td>
</tr>
</tbody>
</table>

### REST API Naming and Addressing

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">17</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >Encoded slash is not used</td>
</tr>
<tr>
<td style="background-color: #555555">18</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >The service interprets values independent of their URL encoding</td>
</tr>
<tr>
<td style="background-color: #555555">19</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >lowerCamelCase is used for names of resources, parameters, and JSON properties</td>
</tr>
</tbody>
</table>

### Service Requests and Responses

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">20</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >REST API - Request and response payloads are in JSON or binary data format</td>
</tr>
<tr>
<td style="background-color: #555555">21</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >REST API - - Since in JSON format, links are relative, links in responses payloads should not contain the schema, hostname, and port. Alternatively, an absolute link can be used, in which case the service must translate the link to the form that goes through the Gateway that is based on the X-Forwarded-* Headers.</td>
</tr>
<tr>
<td style="background-color: #555555">22</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >WebSocket (if applicable) - Service URIs contained in WebSocket messages payload are addressed through the API ML Gateway</td>
</tr>
<tr>
<td style="background-color: #555555">23</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >UI (if applicable) - The UI uses relative links and does not contain the schema, hostname, and port. Alternatively an absolute link can be used, in which case the service must translate the link to the form that goes through the Gateway that is based on the X-Forwarded-* Headers</td>
</tr>
</tbody>
</table>

### Authentication and Authorization

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">24</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >Resources are protected by SAF authorization. All Single-Sign-On methods under item 23 are based on SAF authentication.</td>
</tr>
<tr>
<td rowspan="4" style="background-color: #555555">25</td>
<td colspan="3" style="background-color: #AAAAAA">Please mark which apply (a), (b) or (c)</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA">Services support Single-Sign-On using at least one of the following methods <br />[please mark which apply (a), (b) or (c)]:</td>
</tr>
<tr>
<td style="background-color: #555555">
<p>v2</p>
</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >(a) Services accept PassTickets in the Authorization header of the HTTP requests using the basic authentication scheme (httpBasicPassTicket).</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >(b) Services accept Zowe JWT token in the cookie (zoweJwt)</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >(c) Services accept SAF Identity Token in the cookie (safIdt)</td>
</tr>
</tbody>
</table>

### Versioning and Support

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">26</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >Service implementation follows the semantic versioning model</td>
</tr>
<tr>
<td style="background-color: #555555">27</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >Last two major versions are supported by API services</td>
</tr>
</tbody>
</table>

### WebSocket Services

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">28</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >WebSocket connection creation, all subsequent communication between WebSocket client, and server is routed through the API ML Gateway</td>
</tr>
<tr>
<td style="background-color: #555555">29</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >WebSocket connections are closed by the initiator through API ML Gateway</td>
</tr>
</tbody>
</table>

### Directory and File Ownership Permissions

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">30</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >A conformant application must not modify the contents of the Zowe runtime USS directory and it must not change any directory or file permissions or ownership within the Zowe runtime</td>
</tr>
<tr>
<td style="background-color: #555555">31</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >A conformant application must not modify the permissions or ownership of a Zowe instance directory workspace.&nbsp;&nbsp;</td>
</tr>
</tbody>
</table>

### Packaging

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td colspan="4" style="background-color: #555555">Applicable if LIFECYCLED</td>
<td style="background-color: #555555"></td>
<td style="background-color: #555555">Satisfy the following criteria to lifecycle a service with Zowe. By lifecycling we mean that Zowe Launcher will start, configure, validate and stop the service:</td>
</tr>
<tr>
<td style="background-color: #555555">32</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >If the extension is standalone (not bundled with other products), the extension convenience build (non-SMPE) MUST package itself into zip, tar, or pax format.</td>
</tr>
<tr>
<td style="background-color: #555555">33</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >The extension MUST package a manifest.yaml (or manifest.yml, or manifest.json) into final package.</td>
</tr>
<tr>
<td style="background-color: #555555">34</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >If the extension is standalone (not bundled with other products), the manifest file MUST be placed in the root directory after it&rsquo;s extracted or installed.</td>
</tr>
<tr>
<td style="background-color: #555555">35</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >The extension manifest MUST contain "name" definition.</td>
</tr>
<tr>
<td style="background-color: #555555">36</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >It's recommended to define "version" in the extension manifest.</td>
</tr>
<tr>
<td style="background-color: #555555">37</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >It's recommended to define "license" in the extension manifest .</td>
</tr>
<tr>
<td style="background-color: #555555">38</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >It's recommended to define "title" and "description" in the extension manifest.</td>
</tr>
<tr>
<td style="background-color: #555555">39</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >It's recommended to define "build" in the extension manifest to describe the source code information from version control systems.</td>
</tr>
<tr>
<td style="background-color: #555555">40</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >The extension is suggested to define &ldquo;commands.install&rdquo;, &ldquo;commands.configure&rdquo;, and/or &ldquo;commands.start&rdquo; to instruct Zowe how to install, configure or start in Zowe context.</td>
</tr>
<tr>
<td style="background-color: #555555">41</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >If the extension contains services that will be registered under API-ML, those services MUST be defined as entries of "apimlServices" in the extension manifest.</td>
</tr>
</tbody>
</table>

### Support

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">42</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >Submitter describes how Support is provided and Support details are clearly documented</td>
</tr>
</tbody>
</table>

## Zowe CLI

### Infrastructure 

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">1</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Plug-in is constructed on the Imperative CLI Framework</td>
</tr>
<tr>
<td style="background-color: #555555">2</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Plug-in is NOT run as a standalone CLI</td>
</tr>
<tr>
<td style="background-color: #555555">3</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Plug-in commands write to stdout or stderr via Imperative Framework response.console APIs</td>
</tr>
<tr>
<td style="background-color: #555555">4</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>If plug-in requires gzip decompression support, leverage the Core CLI built-in support -- do NOT opt-out of the built-in gzip decompression support (specifically, the `mDecode` property of the Imperative RestClient must NOT be overridden).</td>
</tr>
<tr>
<td style="background-color: #555555">5</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Plug-ins must not have an @zowe/cli peer dependency for improved npm@7 compatibility. The only peer dependencies that should be included are packages which are imported in the plug-in's source code (e.g., @zowe/imperative).</td>
</tr>
<tr>
<td style="background-color: #555555">6</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>In their Imperative config file (defined in the imperative.configurationModule property of package.json), plug-ins should make their imports as few and specific as possible. This can significantly decrease their load time (<a href="https://github.com/zowe/zowe-cli-db2-plugin/pull/53">example</a>).</td>
</tr>
<tr>
<td style="background-color: #555555">7</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>HTTP or HTTPS requests to REST APIs should use the @zowe/imperative RestClient instead of a direct dependency on a 3rd-party package like request or axios.</td>
</tr>
<tr>
</tbody>
</table>

### Installation

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">8</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Plug-in is installable with the zowe plugins install command</td>
</tr>
<tr>
<td style="background-color: #555555">9</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Plug-in is installable into the @zowe-vN-lts version of the core Zowe CLI and follows semantic versioning (where "N" = the latest "active" LTS release number)</td>
</tr>
<tr>
<td style="background-color: #555555">10</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Plug-in is uninstallable via the zowe plugins uninstall command</td>
</tr>
<tr>
<td style="background-color: #555555">11</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>`@latest` should point to the same version as the most recent zowe lts tag (Note: for V2 it will be `@zowe-v2-lts`)</td>
</tr>
</tbody>
</table>

### Naming

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">12</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>If the plug-in introduces a command group name, it does not conflict with existing conformant plug-in group names</td>
</tr>
<tr>
<td style="background-color: #555555">13</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>Names of CLI commands/groups/options must be in kebab case (lower case &amp; hyphens). Names of properties in zowe.config.json should be camel case. Only alphanumeric characters should be used - `[a-zA-Z0-9-]+`.</td>
</tr>
<tr>
<td style="background-color: #555555">14</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>The following option names/aliases are reserved and must not be used: --response-format-json, --rfj, --help, -h, --help-examples, --help-web, --hw</td>
</tr>
</tbody>
</table>

### Profiles

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">15</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>If the plug-in has unique connection details, it introduces a profile that lets users store these details for repeated use</td>
</tr>
<tr>
<td style="background-color: #555555">16</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>Plug-in users are able to override all profile settings via the command line and/or environment variables</td>
</tr>
<tr>
<td style="background-color: #555555">17</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>If the plug-in uses a Zowe API-ML integrated API, it (the plug-in) has an option named `base-path` in the profile to used to house the path of the associated service in the API ML.</td>
</tr>
<tr>
<td style="background-color: #555555">18</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>If the plug-in connects to a service, it must include the following profile properties AND they MUST be these exact properties (e.g. host, NOT hostname): 'host', 'port', 'user', 'password'</td>
</tr>
<tr>
<td style="background-color: #555555">19</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>If the plug-in connects to a service, and the service supports logging in with a token, it must include the following profile properties AND they MUST be these exact properties: 'tokenType', 'tokenValue'</td>
</tr>
<tr>
<td style="background-color: #555555">20</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>If the plug-in connects to a service, and the service supports logging in with PEM certificates, it must include the following profile properties AND they MUST be these exact properties: 'certFile', 'certKeyFile'</td>
</tr>
<tr>
<td style="background-color: #555555">21</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>If the plug-in connects to a service, and the service supports logging in with PFX/P12 certificates, it must include the following profile properties AND they MUST be these exact properties: 'certFile', 'certFilePassphrase'</td>
</tr>
<tr>
<td style="background-color: #555555">22</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>If the plug-in provides an option to reject untrusted certificates, the property must be named &ldquo;rejectUnauthorized&rdquo;. CLI option should be reject-unauthorized.</td>
</tr>
<tr>
<td style="background-color: #555555">23</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>The plug-in specifies options to be pre-filled by default in zowe.config.json once `zowe config init` has executed</td>
</tr>
<tr>
<td style="background-color: #555555">24</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Plug-in supports team-profile config</td>
</tr>
<tr>
<td style="background-color: #555555">25</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Plug-in supports base profiles</td>
</tr>
<tr>
<td style="background-color: #555555">26</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>When host, port, user, or password is missing for a particular command and no default value is set, the user is prompted for the argument. Host, user, and password should NOT have default values.</td>
</tr>
<tr>
<td style="background-color: #555555">27</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>To take advantage of the new 'zowe config auto-init' command, a plugin that works with a single-sign-on, APIML-compliant REST service MUST supply a new object within its plugin definition to identify that REST service. The new IImperative.apimlConnLookup object must be in the plugin's definition. That object includes the apiId and gatewayUrl of the corresponding REST service. The related REST service must also supply its apiId and gatewayUrl in the apiml section of its application.yml definition. Zowe-CLI automatically handles the apimlConnLookup object for the 'zosmf' service. Thus an apimlConnLookup object for 'zosmf' does not have to be specified within a plugin.</td>
</tr>
</tbody>
</table>

### Support

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">28</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Submitter describes how Support is provided and Support details are clearly documented</td>
</tr>
</tbody>
</table>

### Documentation

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">29</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>Plug-in command help is contributed to this repo for the purpose of hosting the ecosystem web-help on Zowe Docs - <a href="https://github.com/zowe/zowe-cli-web-help-generator">https://github.com/zowe/zowe-cli-web-help-generator</a></td>
</tr>
</tbody>
</table>

## Zowe Application Framework

### Packaging

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">1</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Every plugin must have a unique ID. The ID format follows java package naming conventions. The Zowe project reserves org.zowe</td>
</tr>
<tr>
<td style="background-color: #555555">2</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Every plugin and each of its services must have a version</td>
</tr>
<tr>
<td style="background-color: #555555">3</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Directory layout adheres to the App filesystem structure</td>
</tr>
<tr>
<td style="background-color: #555555">4</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>Source code is also recommended, but not required to adhere to the App filesystem structure for tooling consistency</td>
</tr>
<tr>
<td style="background-color: #555555">5</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Plugins must be packaged as part of a Component, so that Component install &amp; managment tooling can be used</td>
</tr>
<tr>
<td style="background-color: #555555">6</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Plugins must not be installed by calling install-app.sh directly, as Component tooling calls it instead. More information is available in "Packaging" conformance section</td>
</tr>
</tbody>
</table>

### Packaging Format and Manifest

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">7</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>If the extension is standalone (not bundled with other products), the extension convenience build (non-SMPE) MUST package itself into zip, tar, or pax format.</td>
</tr>
<tr>
<td style="background-color: #555555">8</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>The extension MUST package a manifest.yaml (or manifest.yml, or manifest.json) into final package.</td>
</tr>
<tr>
<td style="background-color: #555555">9</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>If the extension is standalone (not bundled with other products), the manifest file MUST be placed in the root directory after it&rsquo;s extracted or installed.</td>
</tr>
<tr>
<td style="background-color: #555555">10</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>The extension manifest MUST contain "name" definition.</td>
</tr>
<tr>
<td style="background-color: #555555">11</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>If the extension manifest contains definition of "appfwPlugins", it MUST also define "id" definition.</td>
</tr>
<tr>
<td style="background-color: #555555">12</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>It's recommended to define "version" in the extension manifest.</td>
</tr>
<tr>
<td style="background-color: #555555">13</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>It's recommended to define "license" in the extension manifest .</td>
</tr>
<tr>
<td style="background-color: #555555">14</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>It's recommended to define "title" and "description" in the extension manifest.</td>
</tr>
<tr>
<td style="background-color: #555555">15</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>It's recommended to define "build" in the extension manifest to describe the source code information from version control systems.</td>
</tr>
<tr>
<td style="background-color: #555555">16</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>The extension is suggested to define &ldquo;commands.install&rdquo;, &ldquo;commands.configure&rdquo;, and/or &ldquo;commands.start&rdquo; to instruct Zowe how to install, configure or start in Zowe context.</td>
</tr>
<tr>
<td style="background-color: #555555">17</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>If the extension contains services that will be registered under API-ML, those services MUST be defined as entries of "apimlServices" in the extension manifest.</td>
</tr>
<tr>
<td style="background-color: #555555">18</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>If the extension contains Zowe App Framework plugin(s), these plugins MUST to defined as entries of "appfwPlugins" in the extension manifest.</td>
</tr>
<tr>
<td style="background-color: #555555">19</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>If the extension contains Zowe ZIS plugin(s), these plugins MUST to defined as entries of "zisPlugins" in the extension manifest.</td>
</tr>
</tbody>
</table>

### Web UIs All

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">20</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>All Apps must contain an icon image file located somewhere within the /web folder of the plugin and the plugin definition must specify the location relative to the /web folder as the webContent.launchDefinition.imageSrc property</td>
</tr>
</tbody>
</table>

### Web UI IFrame

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">21</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>IFrame Apps (apps with framework type "iframe") which embed a top-level iframe within (<a href="https://github.com/zowe/api-layer/blob/master/zlux-api-catalog/web/index.html">example</a>) must use the ID "zluxIframe" for that element. This is required for the app to be a recipient of app to app communication.</td>
</tr>
<tr>
<td style="background-color: #555555">22</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Zowe resources must be accessed via the iframe-adapter located within zlux-app-manager/bootstrap/web. Use of window.parent or window.top to access the ZoweZLUX object is non-permissible.</td>
</tr>
</tbody>
</table>

### Web UI Non-IFrame

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">23</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>DOM elements originating from your App should always be a child of the Zowe viewport DOM element, "com-rs-mvd-viewport"</td>
</tr>
<tr>
<td style="background-color: #555555">24</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Network requests to the Zowe App Server must never be done without the use of the URI Broker</td>
</tr>
<tr>
<td style="background-color: #555555">25</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>Access to resources outside the App Server should also be made through the URI Broker whenever possible</td>
</tr>
<tr>
<td style="background-color: #555555">26</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Apps must not pollute the global namespace with regards to Javascript, HTML, and CSS however it is permitted to have 1 Javascript global who's name is equal to the plugin identifier</td>
</tr>
<tr>
<td style="background-color: #555555">27</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>When using a library present in the Zowe App Framework core, you must depend on the same version, as seen in <a href="https://docs.zowe.org/stable/extend/extend-desktop/mvd-externals/">here</a></td>
</tr>
<tr>
<td style="background-color: #555555">28</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>Web apps should extend the framework's default build scripts for webpack and typescript.</td>
</tr>
</tbody>
</table>

### UI Design

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">29</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>Apps should follow the UI Design guidelines at this <a href="https://github.com/zowe/community/blob/master/Technical-Steering-Committee/guidelines/ui-guidelines.md">page</a></td>
</tr>
</tbody>
</table>

### Localization and Internationalization (l10n and l18n)

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">30</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>If supporting more than one language, the active language to be used for string selection must be retrieved using the get methods in ZoweZLUX.globalization, which determine language by multiple factors</td>
</tr>
<tr>
<td style="background-color: #555555">31</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>If supporting more than one language, no strings visible in a UI should be hard-coded, rather resource strings must be used in accordance with one of the existing internationalization support mechanisms</td>
</tr>
</tbody>
</table>

### App Server

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">32</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Data services should be written such that all synchronous and asynchronous errors are caught. Utilize try-catch and check the existence of error objects from asynchronous calls. Uncaught exceptions effect server responsiveness and disrupt clients</td>
</tr>
</tbody>
</table>

### Documentation

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">33</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Every HTTP API which is intended for 3rd party use must be documented in swagger 2.0. The swagger document must be stored in doc/swagger</td>
</tr>
<tr>
<td style="background-color: #555555">34</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>In addition, it is recommended to have documentation about the format of any Websocket APIs, to be placed within doc</td>
</tr>
</tbody>
</table>

### Logging

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">35</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>An Apps non-IFrame web components, or App Framework dataservices (eg Javascript and Typescript) must log only through the "zlux" logger</td>
</tr>
<tr>
<td style="background-color: #555555">36</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>ZSS services log only through the Zowe ZSS Logger</td>
</tr>
<tr>
<td style="background-color: #555555">37</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Passwords must never be logged</td>
</tr>
<tr>
<td style="background-color: #555555">38</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>Error reporting should follow the standard tooling</td>
</tr>
</tbody>
</table>

### Encoding

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">39</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>If you want your Apps to work with z/OS Node.js version 12 or greater, all application files must be tagged according to their content type</td>
</tr>
</tbody>
</table>

### Storage

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">40</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>For persistent storage, user preferences (if applicable to a plugin) must be stored through the configuration data service</td>
</tr>
<tr>
<td style="background-color: #555555">41</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Regarding persistent storage for other plugin storage needs, storing data outside of the configuration dataservice is permitted only within /workspaceDirectory/app-server or /workspaceDirectory/app-server/pluginStatic with a top-level folder equal to their plugin ID. Plugins must not store information anywhere else in any Zowe directories such as /workspaceDirectory or $ROOT_DIR in order to prevent conflict with future Zowe versions and other plugins</td>
</tr>
<tr>
<td style="background-color: #555555">42</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>It is advisable for the storage of user preferences to use environment variables for locating directories. Use of the workspace directory environment variable is not required, but should be considered to subvert the use of hard-coded paths</td>
</tr>
<tr>
<td style="background-color: #555555">43</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>To be HA compatible, you should use some or all of the storage APIs of Zowe which include but are not limited to the caching service of the API ML, storage API of the App server, and storage API of ZSS</td>
</tr>
</tbody>
</table>

### Directory and File Ownership Permissions

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">44</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>A conformant application must not modify the contents of the Zowe runtime USS directory and it must not change any directory or file permissions or ownership</td>
</tr>
<tr>
<td style="background-color: #555555">45</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>A conformant application must not modify the permissions or ownership of a Zowe workspace directory</td>
</tr>
</tbody>
</table>

### Lifecycling as a Zowe address space

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td colspan="6" style="background-color: #555555">If the service should be lifecycled by Zowe, then:</td>
</tr>
<tr>
<td style="background-color: #555555">46</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>it should provide and specify in its Component manifest a start.sh script</td>
</tr>
<tr>
<td style="background-color: #555555">47</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>a validate.sh script</td>
</tr>
<tr>
<td style="background-color: #555555">48</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>a configure.sh script</td>
</tr>
<tr>
<td style="background-color: #555555">49</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>If the service introduces new environment variables to the zowe.yaml file, these should be prefixed by the provider ID to avoid collisions</td>
</tr>
</tbody>
</table>

### Support

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">50</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Submitter describes how Support is provided and Support details are clearly documented</td>
</tr>
</tbody>
</table>

## Zowe Explorer for Visual Studio Code

### General Extension

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">1</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Naming:</b> If the extension uses the word "Zowe" in its name, it abides by <a href="https://www.linuxfoundation.org/trademark-usage/">The Linux Foundation Trademark Usage Guidelines and Branding Guidelines</a> to ensure the word Zowe is used in a way intended by the Zowe community.</td>
</tr>
<tr>
<td style="background-color: #555555">2</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>No Zowe CLI plugin installation requirement:</b> If the extender makes use of a Zowe CLI profile other than the Zowe Explorer default `zosmf` then the extension must not make any assumptions that a matching Zowe CLI plugin has been installed in the Zowe Explorer user's environment.</td>
</tr>
<tr>
<td style="background-color: #555555">3</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Publication tag:</b> If the extension is published in a public catalog or marketplace such as Npmjs, Open-VSX, or VS Code Marketplace, it uses the tag or keyword "Zowe" so it can be found when searching for Zowe and be listed with other Zowe offerings.</td>
</tr>
<tr>
<td style="background-color: #555555">4</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Support:</b> Extension has documentation with instructions on how to report problems that are related to the extension and not Zowe Explorer. It needs to explain how users can determine if a problem is related to the extension or Zowe Explorer.</td>
</tr>
<tr>
<td style="background-color: #555555">5</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>User settings consistency:</b> Extender provides a consistent user settings experience. For VS Code extensions, extender follows the recommended naming convention for configuration settings as described in VS Code's configuration contribution documentation</td>
</tr>
<tr>
<td style="background-color: #555555">6</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Using .zowe in user settings:</b> Extender avoids starting setting names with the prefix `zowe.`, which is reserved for Zowe Explorer and and other extensions maintained by the Zowe Project .</td>
</tr>
<tr>
<td style="background-color: #555555">7</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>Error message consistency:</b> Extension follows the recommended error message format indicated in the Zowe Explorer extensibility documentation to provide a consistent user experience with Zowe Explorer.</td>
</tr>
<tr>
<td style="background-color: #555555">8</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>Zowe SDK usage:</b> Extension utilizes the available Zowe SDKs that standardize z/OS interactions as well as other common capabilities that are used by many other Zowe extensions and tools unless the extension's goal is to provide a new implementation with clearly stated goals.</td>
</tr>
<tr>
<td style="background-color: #555555">9</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Sharing Zowe profiles:</b> If the  Extension accesses the same mainframe service as a Zowe CLI plug-in, the connection information should be shared via Zowe Team Config (zowe.config.json)</td> 
</tr>
<tr>
<td rowspan="5" style="background-color: #555555">10</td>
<td colspan="4" style="background-color: #555555">Mark (a) (b) (c) (d)</td>
<td style="background-color: #555555">Extension enhances the mainframe user experience [a] <br /> 
OR <br />
Extension utilizes the extensibility APIs provided by Zowe Explorer
 [b, c, d]</td>
</tr>
<tr>
<td style="background-color: #555555"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >a. Extension interacts with mainframe content retrieved via Data Set, USS or Jobs view</td>
</tr>
<tr>
<td style="background-color: #555555"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >b. Extension Accessing Profiles</td>
</tr>
<tr>
<td style="background-color: #555555"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >c. Data Provider Extension</td>
</tr>
<tr>
<td style="background-color: #555555"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >d. Extension Adding Menus</td>
</tr>
</tbody>
</table>

### [a] Extension Interacts with mainframe assets delivered by Zowe Explorer
<p>Criteria for VS Code extensions that  access or interact with Zowe Explorer assets (i.e. data sets, USS, jobs)</p>

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">11</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>README.MD File:</b> Extension documents the following in its associated README.MD file (displayed at the appropriate Marketplace) <br/>
(1) recommends use of Zowe Explorer <br/>
(2) describes the relationship to Zowe Explorer <br/>
(3) describes the scenario  that leverages Zowe Explorer <br/>
(4) uses the "zowe" TAG <br/>
Sample verbiage:  Recommended for use with Zowe Explorer.  [Extension-name] extension uses the Zowe Explorer to access mainframe files and then ....[complete-your-use-case-here]
</td>
</tr>
</tbody>
</table>

### [b] Extension Accessing Profiles
<p>Criteria for VS Code extensions that want to access the same Zowe CLI profiles that Zowe Explorer uses:</p>

<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">12</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>VS Code extension dependency:</b> If the extension calls the Zowe Explorer API it must declare Zowe Explorer as a VS Code extension dependency by including an <code>extensionDependencies</code> entry for Zowe Explorer in its package.json file. This ensures Zowe Explorer and Zowe Explorer API are activated and initialized for proper use by its extenders.
</td>
</tr>
<tr>
<td style="background-color: #555555">13</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Zowe Extender access:</b> Extension accesses the shared Zowe Explorer profiles cache via `ZoweExplorerApi.IApiRegisterClient.getExplorerExtenderApi()` API as documented in the Zowe Explorer extensibility documentation.</td>
</tr>
<tr>
<td style="background-color: #555555">14</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Added Profile Type initialization:</b> If the extension has a dependency on a new Zowe CLI profile type other than the Zowe Explorer default `zosmf`, it is calling the `ZoweExplorerApi.IApiRegisterClient.getExplorerExtenderApi().initialize(profileTypeName)` to ensure that the profile type is supported and managed by the extension without a Zowe CLI plugin installed.</td>
</tr>
<tr>
<td style="background-color: #555555">15</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>Base Profile and Tokens:</b> Extension supports base profiles and tokens</td>
</tr>
<tr>
<td style="background-color: #555555">16</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Team Configuration File:</b> Extension supports the Zowe CLI team configuration file format.</td>
</tr>
<tr>
<td style="background-color: #555555">17</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>v1 Profile Support:</b> Extension has a backwards compatibility and it is able to support v1 type of profiles.</td>
</tr>
</tbody>
</table>

### [c] Extension Serves as a Data Provider

<p>Criteria for VS Code extensions that extend the Zowe Explorer MVS, USS, or JES tree views to use alternative z/OS interaction protocols such as FTP or a REST API.</p>
<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">18</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>VS Code extension dependency:</b> If the extension calls the Zowe Explorer API it must declare Zowe Explorer as a VS Code extension dependency by including an <code>extensionDependencies</code> entry for Zowe Explorer in its package.json file. This ensures Zowe Explorer and Zowe Explorer API are activated and initialized for proper use by its extenders.
</td>
</tr>
<tr>
<td style="background-color: #555555">19</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>New Zowe CLI profile type:</b> Extension registers its new API instances with a new profile type name for the different Zowe Explorer views via the <code>ZoweExplorerApi.IApiRegisterClient.register{Mvs|Uss|Jes}Api(profileTypeName)</code> call as indicated from the Zowe Explorer extensibility documentation</td>
</tr>
<tr>
<td style="background-color: #555555">20</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>Matching Zowe CLI Plugin:</b> Provide a Zowe CLI Plugin for the data provider's new profile type that implements the core capabilities required for the new protocol that users can then also use to interact with the protocol outside of the Zowe Explorer extension using Zowe CLI commands.</td>
</tr>
<tr>
<td style="background-color: #555555">21</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Data provider API implementation:</b> Extension fully implements and registers to at least one of the three Zowe Explorer interfaces or alternatively throw exceptions that provide meaningful error messages to the end-user in the 'Error.message' property that will be displayed in a dialog.</td>
</tr>
<tr>
<td style="background-color: #555555">22</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>API test suite implementation:</b> If the extension implements a Zowe Explorer API data provider interface, it should implement a test suite that calls each of the implemented API methods.</td>
</tr>
</tbody>
</table>

### [d] Extension Adding Menus

<p>Criteria for VS Code extensions adding menu and commands to VS Code that utilize Zowe Explorer data or extend Zowe Explorer capabilities.</p>
<table rules="all">
<thead>
<th style="background-color: #5555AA">Item</th>
<th style="background-color: #5555AA">Version</th>
<th style="background-color: #5555AA">Required</th>
<th style="background-color: #5555AA">Best Practice</th>
<th style="background-color: #5555AA">Conformant</th>
<th style="background-color: #5555AA">Criteria</th>
</thead>
<tbody>
<tr>
<td style="background-color: #555555">23</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>VS Code extension dependency:</b> If the extension calls the Zowe Explorer API it should declare Zowe Explorer as a VS Code extension dependency by including an <code>extensionDependencies</code> entry for Zowe Explorer in its package.json file. This ensures Zowe Explorer and Zowe Explorer API are activated and initialized for proper use by its extenders.
</td>
</tr>
<tr>
<td style="background-color: #555555">24</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Command operations:</b> If the extension is adding new commands to Zowe Explorer's tree views, the commands must not replace any existing Zowe Explorer commands.</td>
</tr>
<tr>
<td style="background-color: #555555">25</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>Command categories 1:</b> If the extension adds to contributes.commands in package.json, the value assigned to the category property contains the extension name.</td>
</tr>
<tr>
<td style="background-color: #555555">26</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Command categories 2:</b> If the extension assigns values to the category property in contributes.commands in package.json, the value cannot be "Zowe Explorer".</td>
</tr>
<tr>
<td style="background-color: #555555">27</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Context menu groups:</b> If contributing commands to Zowe Explorer's context menus, the extension follows the Zowe Explorer extensibility documentation and adds them in new context menu groups that are located below Zowe Explorer's existing context menu groups in the user interface.</td>
</tr>
<tr>
<td style="background-color: #555555">28</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>Adding New Menu Items:</b> If the extension is adding new commands and context menu entries to the Zowe Explorer tree view nodes, the new command name is consistent with the terminology and naming conventions of the existing Zowe Explorer menu entries. More information is provided in the Zowe Explorer extensibility documentation.</td>
</tr>
<tr>
<td style="background-color: #555555">29</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Existing Menu Items:</b> Extension does not overwrite any existing Zowe Explorer command and context menu entries</td>
</tr>
<tr>
<td style="background-color: #555555">30</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Context menu items:</b> If contributing commands to Zowe Explorer's views (such as Data Sets, USS, or Jobs), the extension should only add them to the view's right-click context menus.</td>
</tr>
</tbody>
</table>
