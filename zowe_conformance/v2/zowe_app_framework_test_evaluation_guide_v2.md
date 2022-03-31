# Zowe Application Framework v2 Conformance Test Evaluation Guide

The Zowe Application Framework v2 Conformance Test Evaluation Guide is a set of self-certifying and self-service tests to help the development community integrate and extend specific technology into the Zowe Application Framework. 

Items marked **(required)** are required for an application to be conformant. Items marked **(best practice)** are considered best practices for conformant applications.

These Zowe Application Framework Conformance criteria are applicable to the lastest Zowe v2 LTS Release.

- [Zowe Application Framework v2 Conformance Test Evaluation Guide](#zowe-application-framework-v2-conformance-test-evaluation-guide)
  - [Packaging](#packaging)
  - [Packaging Format and Manifest](#packaging-format-and-manifest)
  - [Web UIs All](#web-uis-all)
  - [Web UI IFrame](#web-ui-iframe)
  - [Web UI Non-IFrame](#web-ui-non-iframe)
  - [UI Design](#ui-design)
  - [Localization and Internationalization (l10n and l18n)](#localization-and-internationalization-l10n-and-l18n)
  - [App Server](#app-server)
  - [Documentation](#documentation)
  - [Logging](#logging)
  - [Encoding](#encoding)
  - [Storage](#storage)
  - [Directory and File Ownership Permissions](#directory-and-file-ownership-permissions)
  - [Lifecycling as a Zowe address space](#lifecycling-as-a-zowe-address-space)
  - [Support](#support)
 
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

## Packaging Format and Manifest

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

## Web UIs All

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

## Web UI IFrame

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

## Web UI Non-IFrame

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

## UI Design

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

## Localization and Internationalization (l10n and l18n)

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

## App Server

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

## Documentation

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

## Logging

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

## Encoding

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

## Storage

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

## Lifecycling as a Zowe address space

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
<td style="background-color: #555555">50</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Submitter describes how Support is provided and Support details are clearly documented</td>
</tr>
</tbody>
</table>