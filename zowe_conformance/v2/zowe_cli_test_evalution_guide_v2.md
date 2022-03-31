# Zowe CLI v2 Conformance Test Evaluation Guide

The Zowe CLI v2 Conformance Test Evaluation Guide is a set of self-certifying and self-service tests to help the development community integrate and extend specific technology into the Zowe CLI. 

Items marked **(required)** are required for an application to be conformant. Items marked **(best practice)** are considered best practices for conformant applications.

These Zowe CLI Conformance criteria are applicable to the lastest Zowe v2 LTS Release.

- [Zowe CLI v2 Conformance Test Evaluation Guide](#zowe-cli-v2-conformance-test-evaluation-guide)
  - [Infrastructure](#infrastructure)
  - [Installation](#installation)
  - [Naming](#naming)
  - [Profiles](#profiles)
  - [Support](#support)
  - [Documentation](#documentation)

## Infrastructure 

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

## Installation

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

## Naming

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

## Profiles

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
<td style="background-color: #555555">28</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td>Submitter describes how Support is provided and Support details are clearly documented</td>
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
<td style="background-color: #555555">29</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td>Plug-in command help is contributed to this repo for the purpose of hosting the ecosystem web-help on Zowe Docs - <a href="https://github.com/zowe/zowe-cli-web-help-generator">https://github.com/zowe/zowe-cli-web-help-generator</a></td>
</tr>
</tbody>
</table>