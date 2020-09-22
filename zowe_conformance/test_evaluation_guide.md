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

    b. Services accept basic authentication (minimum requirement). **(required)**

    c. Single-Sign-On Support: Services accept EITHER Zowe JWT token in the cookie OR support of PassTickets. **(required)**

7.  **Versioning and Support**

    a. Service implementation follows the semantic versioning model. **(best practice)**

    b. The last two major versions are supported by API services. **(required)**

8.  **UI**

    The UI uses only relative URLs. **(required)**

9.  **WebSocket Services**

    a. WebSocket connection creation, all subsequent communication between WebSocket client, and server are routed through the API ML Gateway **(required)**

    b. WebSocket connections are closed by the initiator through API ML Gateway. **(required)**
    
10. **Directory and File Ownership Permissions**

    a. A conformant application must not modify the contents of the Zowe runtime USS directory and it must not change any directory or file permissions or ownership within the Zowe runtime. **(required)**

    b. A conformant application must not modify the permissions or ownership of a Zowe instance directory workspace. **(required)**      
11. **Lifecycling as a Zowe address space**

    a. Satisfy the following criteria to lifecycle a service with Zowe:
    
     - Contains a fully qualified path in the `instance.env` file for the Zowe workspace which points to the location of a directory containing a `start.sh` script. **(required)**
     - Contains a `validate.sh` script. **(best practice)**
     - Contains a `configure.sh` script. **(best practice)**

    b. If the service introduces new variables to the `instance.env` file, these variables should be prefixed by the provider ID to avoid collisions. **(required)**

12. **Support**

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
