# Zowe Explorer v2 Conformance Test Evaluation Guide

The Zowe Explorer v2 Conformance Test Evaluation Guide is a set of self-certifying and self-service tests to help the development community integrate and extend specific technology into the Zowe Explorer. 

Items marked **(required)** are required for an application to be conformant. Items marked **(best practice)** are considered best practices for conformant applications.

These Zowe Explorer Conformance criteria are applicable to the lastest Zowe v2 LTS Release.

- [Zowe Explorer v2 Conformance Test Evaluation Guide](#zowe-explorer-v2-conformance-test-evaluation-guide)
  - [General Extension](#general-extension)
  - [Extension Accessing Profiles](#extension-accessing-profiles)
  - [Data Provider Extension](#data-provider-extension)
  - [Extension Adding Menus](#extension-adding-menus)

## General Extension

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
<td ><b>Sharing of profiles with Zowe CLI:</b> Extensions that utilize Zowe CLI profiles must keep the shared profile instances compatible between Zowe CLI and the Zowe Explorer extension that utilize them.</td>
</tr>
<tr>
<td rowspan="4" style="background-color: #555555">10</td>
<td colspan="3" style="background-color: #555555">Mark (a) (b) (c)</td>
<td style="background-color: #555555"></td>
<td style="background-color: #555555">Extension uses the extensibility APIs provided by Zowe Explorer. Supported methods include (select all that apply a, b, c):</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA">-</td>
<td style="background-color: #AAAAAA">-</td>
<td></td>
<td >a. Extension Accessing Profiles</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA">-</td>
<td style="background-color: #AAAAAA">-</td>
<td></td>
<td >b. Data Provider Extension</td>
</tr>
<tr>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA">-</td>
<td style="background-color: #AAAAAA">-</td>
<td></td>
<td >c. Extension Adding Menus</td>
</tr>
</tbody>
</table>

## Extension Accessing Profiles

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
<td style="background-color: #555555">11</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>VS Code extension dependency:</b> Extension declares Zowe Explorer as a VS Code extension dependency by including an `extensionDependencies` entry for Zowe Explorer in its package.json file.</td>
</tr>
<tr>
<td style="background-color: #555555">12</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Zowe Extender access:</b> Extension accesses the shared Zowe Explorer profiles cache via `ZoweExplorerApi.IApiRegisterClient.getExplorerExtenderApi()` API as documented in the Zowe Explorer extensibility documentation.</td>
</tr>
<tr>
<td style="background-color: #555555">13</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Added Profile Type initialization:</b> If the extension has a dependency on a new Zowe CLI profile type other than the Zowe Explorer default `zosmf`, it is calling the `ZoweExplorerApi.IApiRegisterClient.getExplorerExtenderApi().initialize(profileTypeName)` to ensure that the profile type is supported and managed by the extension without a Zowe CLI plugin installed.</td>
</tr>
<tr>
<td style="background-color: #555555">14</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>Base Profile and Tokens:</b> Extension supportsbase profilesandtokens</td>
</tr>
<tr>
<td style="background-color: #555555">15</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Team Configuration File:</b> Extension supports the Zowe CLI 7 team configuration file format.</td>
</tr>
<tr>
<td style="background-color: #555555">16</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>v1 Profile Support:</b> Extension has a backwards compatibility and it is able to support v1 type of profiles.</td>
</tr>
<tr>
<td style="background-color: #555555">17</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Secure Credential Store:</b> Extension calls theZowe Explorer-provided methodfor initialization of secure credentials at startup.</td>
</tr>
</tbody>
</table>

## Data Provider Extension

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
<td ><b>New Zowe CLI profile type:</b> Extension registers its new API instances with a new profile type name for the different Zowe Explorer views via the `ZoweExplorerApi.IApiRegisterClient.register{Mvs|Uss|Jes}Api(profileTypeName)` call as indicated from the Zowe Explorer extensibility documentation</td>
</tr>
<tr>
<td style="background-color: #555555">19</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>Matching Zowe CLI Plugin:</b> Provide a Zowe CLI Plugin for the data provider's new profile type that implements the core capabilities required for the new protocol that users can then also use to interact with the protocol outside of the Zowe Explorer extension using Zowe CLI commands.</td>
</tr>
<tr>
<td style="background-color: #555555">20</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Data provider API implementation:</b> Extension fully implements and registers to at least one of the three Zowe Explorer interfaces or alternatively throw exceptions that provide meaningful error messages to the end-user in the 'Error.message' property that will be displayed in a dialog.</td>
</tr>
<tr>
<td style="background-color: #555555">21</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>API test suite implementation:</b> If the extension implements a Zowe Explorer API data provider interface, it should implement a test suite that calls each of the implemented API methods.</td>
</tr>
</tbody>
</table>

## Extension Adding Menus

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
<td style="background-color: #555555">22</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Command operations:</b> If the extension is adding new commands to Zowe Explorer's tree views, the commands must not replace any existing Zowe Explorer commands.</td>
</tr>
<tr>
<td style="background-color: #555555">23</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>Command categories 1:</b> If the extension adds to contributes.commands in package.json, the value assigned to the category property contains the extension name.</td>
</tr>
<tr>
<td style="background-color: #555555">24</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Command categories 2:</b> If the extension assigns values to the category property in contributes.commands in package.json, the value cannot be "Zowe Explorer".</td>
</tr>
<tr>
<td style="background-color: #555555">25</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Context menu groups:</b> If contributing commands to Zowe Explorer's context menus, the extension follows theZowe Explorer extensibility documentationand adds them in new context menu groups that are located below Zowe Explorer's existing context menu groups in the user interface.</td>
</tr>
<tr>
<td style="background-color: #555555">26</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"></td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td></td>
<td ><b>Adding New Menu Items:</b> If the extension is adding new commands and context menu entries to the Zowe Explorer tree view nodes, the new command name is consistent with the terminology and naming conventions of the existing Zowe Explorer menu entries. More information is provided in the Zowe Explorer extensibility documentation.</td>
</tr>
<tr>
<td style="background-color: #555555">27</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Existing Menu Items:</b> Extension does not overwrite any existing Zowe Explorer command and context menu entries</td>
</tr>
<tr>
<td style="background-color: #555555">28</td>
<td style="background-color: #555555">v2</td>
<td style="background-color: #AAAAAA"><center>x</center></td>
<td style="background-color: #AAAAAA"></td>
<td></td>
<td ><b>Context menu items:</b> If contributing commands to Zowe Explorer's views (such as Data Sets, USS, or Jobs), the extension should only add them to the view's right-click context menus.</td>
</tr>
</tbody>
</table>