# Zowe Conformance Test Evaluation Guide

The Zowe Conformance Test Evaluation Guide is a set of self-certifying and self-service tests to help the development community integrate and extend specific technology into the Zowe framework. 

This guide describes the requirements of the three available conformance programs. Items marked **(required)** are required to achieve conformance in a given program. Items marked **(best practice)** are considered a best practice for conformant applications.

These Zowe Conformant criteria are applicable to the lastest Zowe v1 LTS Release.

## Zowe API Mediation layer - Zowe v1

1. **Application Service**

    An application provides at least one service or UI registered with discovery services. **(required)**

2. **Register with discovery services**

    a. A service must be registered using one of the following methods:
      - Dynamic registration **(best practice)**
      - Static definition **(required)**

    b. The service must provide a default service ID that is prefixed by the oganization/provider name. **(required)**
    
    * **Examples of compliant service IDs:**\
      `zowemonitoring`, `cajclcheck`, `ibmims`, `rocketterasam`
    * **Examples of non-compliant service IDs:**\
      `jclcheck`, `myims`, `mydb2`
      
    **Note:** The API ID is not part of the URL.
        
    c. The service ID must be configurable externally after deployment. **(required)**
    
    d. The service ID must written in lower case, contain no symbols, and have a maximum of 64 characters. **(required)**

    e. The API ID must follow the same rules as Java packages. **(required)**
    
    * **Example of an API ID:** `org.zowe.apiml.apicatalog`. 

    f. The published service URL must follow the gateway URL conventions. **(required)**

    g. For versioned APIs, the service URL must contain a service version before the service ID in the following formats - **(required)**:
       
    * api/v1/{serviceId} reserved for REST APIs
    * ui/v1/{serviceId} reserved for UIs
    * ws/v1/{serviceId} reserved for WebSockets
    
       For non-versioned APIs or APIs versioned differently (e.g. z/OSMF),
    use the following formats:
    
    * api/{serviceId} reserved for REST APIs
    * ui/{serviceId} reserved for UIs
    * ws/{serviceId} reserved for WebSockets
   
    h. Registration of the service must not be performed by modifying the Zowe runtime directory api-defs folder. Registration can be performed in one of the following ways - **(required)**:
    
    - Adding the static API definition YAML file path to `instance.env` file for the Zowe workspace
    - Copying the static API definition YAML file to the instance directory workspace `api-definitions` directory

3. **API Documentation**

    a. Documentation is Swagger/Open API 2.0/Open API 3.0 compliant. **(required)**

    b. Every public resource is documented with a description of each resource. **(required)**

    c. Every method of each REST endpoint is documented. **(required)**

    d. Every method of each REST endpoint is demonstrated by an example. **(required)**

    e. Every parameter (headers, query parameters, payload, cookies, etc.) is documented with definitions of all possible values and their associated meanings. **(required)**

    f. Every HTTP error code must be documented. If the endpoint has additional more granular error codes, only provide the  documentation reference. **(required)**

4. **API naming and addressing**

    a. Encoded slash is not used. **(best practice)**

    b. The service interprets values independent of their URL encoding. **(required)**

    c. lowerCamelCase is used for names of resources, parameters, and JSON properties. **(best practice)**

5. **Service requests and responses**

    a. API - Request and response payloads are in JSON or binary data format. **(best practice)**

    b. API - In JSON format, links are relative, and must not contain the schema, hostname, and port. **(required)**

    c. WebSocket - Service URIs contained in WebSocket messages payload are addressed through the API ML Gateway. **(required)**

    d. UI - The UI uses relative links and does not contain the schema, hostname, and port. **(required)**

6.  **Authentication and Authorization**

    a. Resources are protected by mainframe credentials. **(required)**

    b. Services accept basic authentication or Single-Sign-On Support as explained in the point 6.c (minimum requirement). **(required)**

    c. Single-Sign-On Support: Services accept EITHER Zowe JWT token in the cookie OR support of PassTickets. **(required)**

7.  **Versioning and Support**

    a. Service implementation follows the semantic versioning model. **(best practice)**

    b. The last two major versions are supported by API services. **(required)**

8.  **WebSocket Services**

    a. WebSocket connection creation, all subsequent communication between WebSocket client, and server are routed through the API ML Gateway **(required)**

    b. WebSocket connections are closed by the initiator through API ML Gateway. **(required)**
    
9. **Directory and File Ownership Permissions**

    a. A conformant application must not modify the contents of the Zowe runtime USS directory and it must not change any directory or file permissions or ownership within the Zowe runtime. **(required)**

    b. A conformant application must not modify the permissions or ownership of a Zowe instance directory workspace. **(required)**      

10. **Lifecycling as a Zowe address space**

    a. Satisfy the following criteria to lifecycle a service with Zowe:
    
     - Contains a fully qualified path in the `instance.env` file for the Zowe workspace which points to the location of a directory containing a `start.sh` script. **(required)**
     - Contains a `validate.sh` script. **(best practice)**
     - Contains a `configure.sh` script. **(best practice)**

    b. If the service introduces new variables to the `instance.env` file, these variables should be prefixed by the provider ID to avoid collisions. **(required)**

11. **Support**

    The Submitter describes how Support is provided. Support details must be clearly documented. **(required)**

## Zowe CLI - Zowe v1

1.  **Infrastructure**

    a. The plug-in is constructed on the Imperative CLI Framework. **(required)**

    b. The plug-in does NOT run as a standalone CLI (e.g. It does not specify a bin field in the `package.json` or other similar technique to run as a standalone.) **(required)**

    c. The plug-in commands write to `stdout` or `stderr` via Imperative Framework `response.console` APIs. **(required)**

2.  **Installation**

    a. The plug-in is installable with the zowe plugins install command. **(required)**

    b. The plug-in is installable into the \@zowe-v1-lts version of the core Zowe CLI and follows semantic versioning. **(required)**

    c. The plug-in is uninstallable via the zowe plugins uninstall command. **(required)**

3.  **Naming**

    If the plug-in introduces a command group name, it does not conflict with existing conformant plug-in group names. **(required)**

4.  **Profiles**

    a. If the plug-in has unique connection details, it introduces a profile that lets users store these details for repeated use. **(required)**

    b. The plug-in users are able to override all profile settings via the command line and/or environment variables. **(best practice)**

5.  **Support**

    The Submitter describes how Support is provided. Support details must be clearly documented.

## Zowe App Framework -- Zowe v1

1.  **Packaging**

    a. Every plug-in must have a unique ID. The ID format follows java package naming conventions. The Zowe project reserves org.zowe. **(required)**

    b. Every plug-in and each of its services must have a version. **(required)**

    c. The directory layout adheres to the App filesystem structure. **(required)**

    d. Source code layout is recommended, but not required to adhere to the App filesystem structure for tooling consistency. **(best practice)**

2.  **Web UIs ALL**

    All Apps must contain an icon image file to represent it, located at web/assets/icon.png within the App's package. **(required)**

3.  **Web UI IFrame**

    a. IFrame Apps (apps with framework type \"iframe\") which embed a top-level iframe within them must use the ID \"zluxIframe\" for that element. This is required for the app to be a recipient of app to app communication. **(required)**
    
    * **Example:** <https://github.com/zowe/api-layer/blob/master/zlux-api-catalog/web/index.html>)

    b. Zowe resources must be accessed via the iframe-adapter located within `zlux-app-manager/bootstrap/web`. Use of `window.parent` or `window.top` to access the ZoweZLUX object is non-permissible. **(required)**

    c.  Documentation or automated addition of the "iframe" plug-in to the Zowe desktop must be performed by executing the script 'zowe-install-app.sh' script in the Zowe instance directory. **(required)**

4.  **Web UI Non-IFrame**

    a. DOM elements originating from your App should always be children of the Zowe viewport DOM element, `com-rs-mvd-viewport`. **(required)**

    b. Network requests to the Zowe App Server must never be done without the use of the URI Broker. This ensures compatibility with future versions of Zowe if URLs change. **(required)**

    c. Access to resources outside the App Server should also be made through the URI Broker whenever possible. **(best practice)**

    d. Apps must not pollute the global namespace with regards Javascript, HTML, and CSS. **(required)**

    e. When using a library present in the Zowe App Framework core, you must depend on the same version. **(required)**

    f. Web apps should extend the framework's default build scripts for webpack and typescript. **(required)**
5.  **UI Design**

    Apps should follow the UI Design guidelines at <https://github.com/zowe/zlc/blob/master/process/UI_GUIDELINES.md>. **(best practice)**

6.  **Localization and Internationalization (I10n and I18n)**

    a. If your software supports multiple languages, the active language to be used for string selection must be retrieved using ZoweZLUX.globalization.getLanguage(), which determines language by multiple factors. **(required)**

    b. No strings visible in a UI should be hard-coded, rather resource strings must be used in accordance with one of the existing internationalization support mechanisms. **(best practice)**

7.  **App Server**

    a. Data services should be written such that all synchronous and asynchronous errors are caught. Utilize try-catch and check the existence of error objects from asynchronous calls. Uncaught exceptions affect server responsiveness and disrupt clients. **(required)**

8.  **Documentation**

    a. Every HTTP API must be documented in swagger 2.0. The swagger document must be stored in doc/swagger. **(required)**

    b. In addition, we recommend documentation about the format of any Websocket APIs, to be placed within the doc. **(best practice)**

9.  **Logging**

    a. An Apps non-IFrame web components, or App Framework dataservices (e.g. Javascript and Typescript) must log only through the "zlux" logger. **(required)**

    b. ZSS services log only through the Zowe ZSS Logger. **(required)**

    c. Passwords must never be logged. **(required)**

    d. Error reporting should follow the standard tooling. **(best practice)**
    
10. **Encoding**

    a. Application Framework plugins serving web content through App Server or doing file I/O through an App Server dataservice should tag these files on z/OS according to their content type. **(best practice)**
    
    b. Testing Apps via the install-app script is advisable to enable end users to utilize Zowe plugin management tooling. **(best practice)**

11. **Storage**

    a. User preferences, if applicable to a plug-in, must be stored through the configuration data service, unless the software needs pre-existing storage structures such as DB2 **(required)**

    b. For other plug-in storage needs, storing data outside of the configuration dataservice is permitted only within `$INSTANCE_DIR/workspace/app-server` or `$INSTANCE_DIR/workspace/app-server/pluginStatic` with a top-level folder equal to their plug-in ID. Plug-ins must not store information anywhere else in any Zowe directories such as `$INSTANCE_DIR` or `$ROOT_DIR` in order to prevent conflict with future Zowe versions and other plug-ins. **(required)**

    c. It is advisable for the storage of user preferences to use environment variables for locating directories. Use of the instance directory environment variable is not required, however, we recommend the use of this variable to subvert the use of hard-coded paths. **(best practice)**

12. **Directory and File Ownership Permissions**

    a. A conformant application must not modify the contents of the Zowe root directory (`$ROOT_DIR`) and must not change any directory or file permissions or ownership. **(required)**

    b. A conformant application must not modify the permissions or ownership of a Zowe instance directory workspace. **(best practice)**

13. **Lifecycling as a Zowe address space**

    a. If the app framework plugin requires services that do not originate from Zowe, but require the same lifecycle as Zowe, satisfy the following criteria to lifecycle them with Zowe:
    
     - Contain a fully qualified path in the `instance.env` file for the Zowe workspace which points to the location of a directory containing a `start.sh` script. **(required)**
     - Contain a validate.sh script. **(best practice)**
     - Contain a configure.sh script. **(best practice)**

    b. If the service introduces new variables to the `instance.env` file, these variables should be prefixed by the provider ID to avoid collisions. **(required)**

14. **Support**

    The Submitter describes how Support is provided. Support details must be clearly documented.


##  Zowe Explorer for Visual Studio Code - Zowe v1

Throughout the this Zowe Explorer for Visual Studio Code section you will find the following terminology being used:

- <a id="extender"></a> _Extender_: The organization or developer producing an extension for Zowe Explorer for Visual Studio Code.
- <a id="extension"></a> _Extension of Zowe Explorer for Visual Studio Code_: An installable piece of software that provides new functionality to Zowe Explorer for Visual Studio Code or uses/calls services provided by Zowe Explorer for Visual Studio Code. Also simply referred to here as an "extension", this can be a Visual Studio Code extension as well as a Zowe CLI Plugin or an independent piece of software. The conformance criteria below call out conformance requirements for three common types of extensions of Zowe Explorer for Visual Studio Code, but it is possible that more kinds of extensions can be created. If such new extension kinds surface, then Zowe Explorer for Visual Studio Code APIs and this document can be expanded to support them in the future.
- _Zowe Explorer for Visual Studio Code - Visual Studio Code extension_: Refers to a Zowe Explorer for Visual Studio Code extension that is a Visual Studio Code extension that is installed in addition to Zowe Explorer for Visual Studio Code ad that has a Visual Studio Code extension dependency to Zowe Explorer for Visual Studio Code.
- <a id="zowe-sdk"></a> _Zowe SDKs_ are [SDKs published by the Zowe project](https://docs.zowe.org/stable/user-guide/sdks-using) that provides various APIs for writing Zowe-based capabilities in general.

1. **General Extension**

    General conformance criteria for all extensions that add new capabilities to Zowe Explorer for Visual Studio Code.

    a. If the extension uses the word "Zowe" in its name, it abides by The Linux Foundation <a href="https://www.linuxfoundation.org/trademark-usage/">Trademark Usage Guidelines</a> and <a href="https://www.openmainframeproject.org/branding-guidelines">Branding Guidelines</a> to ensure the word Zowe is used in a way intended by the Zowe community. **(required)**

    b. No Zowe CLI plugin installation requirement: </b> If the <a href="#extender">extender</a> makes use of a Zowe CLI profile other than the Zowe Explorer for Visual Studio Code default `zosmf` then the extension must not make any assumptions that a matching Zowe CLI plugin has been installed in the Zowe Explorer for Visual Studio Code user's environment. **(best practice)**

    c. **Publication tag:** If the extension is published in a public catalog or marketplace such as Npmjs, Open-VSX, or Visual Studio Code Marketplace, it uses the tag or keyword "Zowe" so it can be found when searching for Zowe and be listed with other Zowe offerings. **(required)**

    d. **Support:** Extension has documentation with instructions on how to report problems that are related to the extension and not Zowe Explorer for Visual Studio Code. It needs to explain how users can determine if a problem is related to the extension or Zowe Explorer for Visual Studio Code. **(required)**

    e. **User settings consistency:** <a href="#extender">Extender</a> provides a consistent user settings experience. For Visual Studio Code extensions, <a href="#extender">extender</a> follows the recommended naming convention for configuration settings as described in Visual Studio Code's <a href="https://code.visualstudio.com/api/references/contribution-points#contributes.configuration">configuration contribution documentation</a>, and avoids starting setting names with the prefix `zowe.`, which is reserved for Zowe Explorer for Visual Studio Code. **(best practice)**

    f. **Error message consistency:** Extension follows the recommended error message format indicated in the Zowe Explorer for Visual Studio Code extensibility documentation to provide a consistent user experience with Zowe Explorer for Visual Studio Code. **(best practice)**

    g. **Zowe SDK usage:** Extension utilizes the available Zowe SDKs that standardize z/OS interactions as well as other common capabilities that are used by many other Zowe extensions and tools unless the extension's goal is to provide a new implementation with clearly stated goals. **(best practice)**

    h. **Sharing of profiles with Zowe CLI:** Extensions that utilize Zowe CLI profiles must share the created profile instances between Zowe CLI and the Zowe Explorer for Visual Studio Code extension that utilize them. **(required)**

    i. Extension uses the extensibility APIs provided by Zowe Explorer for Visual Studio Code. Supported methods include (Please select all that apply):
    - Extension Accessing Profiles
    - Data Provider Extension
    - Extension Adding Menus

2. **Extension Accessing Profiles**

    Criteria for Visual Studio Code extensions that want to access the same Zowe CLI profiles that Zowe Explorer for Visual Studio Code uses.

    a. **Visual Studio Code extension dependency:** Extension declares Zowe Explorer for Visual Studio Code as a Visual Studio Code extension dependency by including an `extensionDependencies` entry for Zowe Explorer for Visual Studio Code in its package.json file. **(required)**

    b. **Zowe <a href="#extender">Extender</a> access:** Extension accesses the shared Zowe Explorer for Visual Studio Code profiles cache via `ZoweExplorerApi.IApiRegisterClient.getExplorerExtenderApi()` API as documented in the Zowe Explorer for Visual Studio Code extensibility documentation. **(required)**

    c. **Added Profile Type initialization:** If the extension has a dependency on a new Zowe CLI profile type other than the Zowe Explorer for Visual Studio Code default `zosmf`, it is calling the `ZoweExplorerApi.IApiRegisterClient.getExplorerExtenderApi().initialize(profileTypeName)` to ensure that the profile type is supported and managed by the extension without a Zowe CLI plugin installed. **(required)**

3. **Data Provider Extension**

    Criteria for Visual Studio Code extensions that extend the Zowe Explorer for Visual Studio Code MVS, USS, or JES tree views to use alternative z/OS interaction protocols such as FTP or a REST API.

    a. **New Zowe CLI profile type:** Extension registers its new API instances with a new profile type name for the different Zowe Explorer for Visual Studio Code views via the `ZoweExplorerApi.IApiRegisterClient.register{Mvs|Uss|Jes}Api(profileTypeName)` call as indicated from the Zowe Explorer for Visual Studio Code extensibility documentation. **(required)**

    b. **Matching Zowe CLI Plugin:** Provide a Zowe CLI Plugin for the data provider's new profile type that implements the core capabilities required for the new protocol that users can then also use to interact with the protocol outside of the Zowe Explorer for Visual Studio Code extension using Zowe CLI commands. **(best practice)**

    c. **Data provider API implementation:** Extension fully implements and registers to at least one of the three Zowe Explorer for Visual Studio Code interfaces or alternatively throw exceptions that provide meaningful error messages to the end-user in the 'Error.message' property that will be displayed in a dialog. **(required)**

    d. **API test suite implementation:**  If the extension implements a Zowe Explorer for Visual Studio Code API data provider interface, it should implement a test suite that calls each of the implemented API methods. **(best practice)**

    e. **Base Profile and Tokens:** Extension supports base profiles and tokens. **(best practice)**

    f. **Team Configuration File:** Extension supports the Zowe CLI 7 team configuration file format as an alternative to the Zowe CLI 6 profiles file format. **(best practice)**

    g. **Secure Credential Store:** If the extension supports Zowe CLI's Secure Credential store, it calls the Zowe Explorer for Visual Studio Code-provided method for initialization at startup. **(best practice)**

4. **Extension Adding Menus**

    Criteria for Visual Studio Code extensions adding menu and commands to Visual Studio Code that utilize Zowe Explorer for Visual Studio Code data or extend Zowe Explorer for Visual Studio Code capabilities.

    a. **Command operations:** If the extension is adding new commands to Zowe Explorer for Visual Studio Code's tree views, the commands must not replace any existing Zowe Explorer for Visual Studio Code commands. **(required)**

    b. **Command categories:** If the extension adds to `contributes.commands` in `package.json`, the value assigned to the `category` property contains the extension name and it cannot be "Zowe Explorer for Visual Studio Code". **(required)**

    c. **Context menu groups:** If contributing commands to Zowe Explorer for Visual Studio Code's context menus, the extension follows the Zowe Explorer for Visual Studio Code extensibility documentation and adds them in new context menu groups that are located below Zowe Explorer for Visual Studio Code's existing context menu groups in the user interface. **(required)**

    d. **Menu Names:** If the extension is adding new commands and context menu entries to the Zowe Explorer for Visual Studio Code tree view nodes, the new command name is consistent with the terminology and naming conventions of the existing Zowe Explorer for Visual Studio Code menu entries. **(best practice)**

    e. **Context menu items:** If contributing commands to Zowe Explorer for Visual Studio Code's views (such as Data Sets, USS, or Jobs), the extension should only add them to the view's right-click context menus. **(best practice)**

