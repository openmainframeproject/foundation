# Zowe APIML v2 Conformance Test Evaluation Guide

The Zowe APIML v2 Conformance Test Evaluation Guide is a set of self-certifying and self-service tests to help the development community integrate and extend specific technology into the Zowe APIML. 

Items marked **(required)** are required for an application to be conformant. Items marked **(best practice)** are considered best practices for conformant applications.

These Zowe APIML Conformance criteria are applicable to the lastest Zowe v2 LTS Release.

- [Zowe APIML v2 Conformance Test Evaluation Guide](#zowe-apiml-v2-conformance-test-evaluation-guide)
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

## Application Service 

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

## REST API Documentation

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
</tbody>
</table>

## REST API Naming and Addressing

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
<td style="background-color: #555555">16</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >Encoded slash is not used</td>
</tr>
<tr>
<td style="background-color: #555555">17</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >The service interprets values independent of their URL encoding</td>
</tr>
<tr>
<td style="background-color: #555555">18</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >lowerCamelCase is used for names of resources, parameters, and JSON properties</td>
</tr>
</tbody>
</table>

## Service Requests and Responses

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
<td style="background-color: #555555">19</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >REST API - Request and response payloads are in JSON or binary data format</td>
</tr>
<tr>
<td style="background-color: #555555">20</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >REST API - - Since in JSON format, links are relative, links in responses payloads should not contain the schema, hostname, and port. Alternatively, an absolute link can be used, in which case the service must translate the link to the form that goes through the Gateway that is based on the X-Forwarded-* Headers.</td>
</tr>
<tr>
<td style="background-color: #555555">21</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >WebSocket (if applicable) - Service URIs contained in WebSocket messages payload are addressed through the API ML Gateway</td>
</tr>
<tr>
<td style="background-color: #555555">22</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >UI (if applicable) - The UI uses relative links and does not contain the schema, hostname, and port. Alternatively an absolute link can be used, in which case the service must translate the link to the form that goes through the Gateway that is based on the X-Forwarded-* Headers</td>
</tr>
</tbody>
</table>

## Authentication and Authorization

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
<td >Resources are protected by SAF authorization. All Single-Sign-On methods under item 23 are based on SAF authentication.</td>
</tr>
<tr>
<td rowspan="4" style="background-color: #555555">24</td>
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

## Versioning and Support

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
<td style="background-color: #555555">25</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >Service implementation follows the semantic versioning model</td>
</tr>
<tr>
<td style="background-color: #555555">26</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >Last two major versions are supported by API services</td>
</tr>
</tbody>
</table>

## WebSocket Services

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
<td style="background-color: #555555">27</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >WebSocket connection creation, all subsequent communication between WebSocket client, and server is routed through the API ML Gateway</td>
</tr>
<tr>
<td style="background-color: #555555">28</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >WebSocket connections are closed by the initiator through API ML Gateway</td>
</tr>
</tbody>
</table>

## Directory and File Ownership Permissions

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
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >A conformant application must not modify the contents of the Zowe runtime USS directory and it must not change any directory or file permissions or ownership within the Zowe runtime</td>
</tr>
<tr>
<td style="background-color: #555555">30</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >A conformant application must not modify the permissions or ownership of a Zowe instance directory workspace.&nbsp;&nbsp;</td>
</tr>
</tbody>
</table>

## Packaging

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
<td style="background-color: #555555">31</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >If the extension is standalone (not bundled with other products), the extension convenience build (non-SMPE) MUST package itself into zip, tar, or pax format.</td>
</tr>
<tr>
<td style="background-color: #555555">32</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >The extension MUST package a manifest.yaml (or manifest.yml, or manifest.json) into final package.</td>
</tr>
<tr>
<td style="background-color: #555555">33</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >If the extension is standalone (not bundled with other products), the manifest file MUST be placed in the root directory after it&rsquo;s extracted or installed.</td>
</tr>
<tr>
<td style="background-color: #555555">34</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >The extension manifest MUST contain "name" definition.</td>
</tr>
<tr>
<td style="background-color: #555555">35</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >It's recommended to define "version" in the extension manifest.</td>
</tr>
<tr>
<td style="background-color: #555555">36</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >It's recommended to define "license" in the extension manifest .</td>
</tr>
<tr>
<td style="background-color: #555555">37</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >It's recommended to define "title" and "description" in the extension manifest.</td>
</tr>
<tr>
<td style="background-color: #555555">38</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >It's recommended to define "build" in the extension manifest to describe the source code information from version control systems.</td>
</tr>
<tr>
<td style="background-color: #555555">39</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >The extension is suggested to define &ldquo;commands.install&rdquo;, &ldquo;commands.configure&rdquo;, and/or &ldquo;commands.start&rdquo; to instruct Zowe how to install, configure or start in Zowe context.</td>
</tr>
<tr>
<td style="background-color: #555555">40</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td >If the extension contains services that will be registered under API-ML, those services MUST be defined as entries of "apimlServices" in the extension manifest.</td>
</tr>
</tbody>
</table>

## Support

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
<td style="background-color: #555555">41</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td >Submitter describes how Support is provided and Support details are clearly documented</td>
</tr>
</tbody>
</table>