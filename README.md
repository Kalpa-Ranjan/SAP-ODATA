



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QECOAB7I%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T062343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMenNmoM%2ByrFDrKnrbExvH7CueA2YOCfpLf7jMy3RLMwIhANJsVnnsJuj7wjUL0KE9seiHA4A7%2BtHn2zlAe1CJH3jtKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyQslCFiQv%2FBpz1w5Eq3AOwN9XUe5kpBCTeqNLzAN9tLoyRtlSiltqfa1sCq4wFW1F5JOLSqndGEadqyO%2F8VWYD4jGbI4iCqA96HrVPPPBHuBqYFUozPoQdtBypcL76hAF4A1jhrFroXr9cpHB12zm4GVIKkZC2CZCCawRPakWgIxp4qDHo368AdZZXzCVb4oUNBlwMFGxjQrP%2BKoQDHY%2Fvr3Of8buDQ1ez4wyzZ2Nutk3V%2Bh5OiG%2BFYvOLUste%2B9hsqQ0ElfE1YRhFGe8j6%2BE165Kdf2DE362Dvx44OVFDpIB%2BhNP%2BYfxCUt7Kd8MoV1g1D6tRwSgk5MsfiRISJH6%2B3Cpots%2B7WiHCct7QFIVuqoDFmbj30BlakvKIIWI3qrZK0CrmoAVYPbjUXRYJPufaBuMNlzWJSCV%2FVL%2ByMjXjU%2BgpWgTz7kra5w0VxToJ0rrThan5gecnI1QP5qaUbpTID8x8Po94RSFMAyrUKDx95CgN7hA%2BeDmIL0%2BWr83wflgs9aEzt2TcHryvOl5uxT1%2Fa1yF3CcbEzn2ixNQLDOQueAHRXS3xAfHcrmhh1VJZu%2Fft2Ey95O4vkJ1pXBw%2BH27JNB6dXHbavW6%2B30V3PDb1jqijWCbolpVYJ3Sbf1fCariArf%2BkJKG3DrPyzCF16vIBjqkAWwoBNBkmvStjp9PT5kINGyXwUjoC920x1Ru5zBQwsBPkASqPSmfiAGU1ilS8k2VwVR0hCsu2Skfqo%2F4D2NDH8UPqDvgBngbw7Ay5O%2BFZTMCmkp1Egn5WlNro6lskLqumBmcaPQERW%2F6UZe5XM5jQZtQ1eVF2SV1EPm5eUS7kzXwU8S4vCPurpUQ0YmRpx%2FGL7oXJjVK6JfOIFIGza%2BG%2FnqGXVEY&X-Amz-Signature=15eb0a988c0f6f925d6e13cd8698403bb223a01d188f12f4149805a73002a370&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QECOAB7I%2F20251105%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251105T062343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEL7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDMenNmoM%2ByrFDrKnrbExvH7CueA2YOCfpLf7jMy3RLMwIhANJsVnnsJuj7wjUL0KE9seiHA4A7%2BtHn2zlAe1CJH3jtKogECIf%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgyQslCFiQv%2FBpz1w5Eq3AOwN9XUe5kpBCTeqNLzAN9tLoyRtlSiltqfa1sCq4wFW1F5JOLSqndGEadqyO%2F8VWYD4jGbI4iCqA96HrVPPPBHuBqYFUozPoQdtBypcL76hAF4A1jhrFroXr9cpHB12zm4GVIKkZC2CZCCawRPakWgIxp4qDHo368AdZZXzCVb4oUNBlwMFGxjQrP%2BKoQDHY%2Fvr3Of8buDQ1ez4wyzZ2Nutk3V%2Bh5OiG%2BFYvOLUste%2B9hsqQ0ElfE1YRhFGe8j6%2BE165Kdf2DE362Dvx44OVFDpIB%2BhNP%2BYfxCUt7Kd8MoV1g1D6tRwSgk5MsfiRISJH6%2B3Cpots%2B7WiHCct7QFIVuqoDFmbj30BlakvKIIWI3qrZK0CrmoAVYPbjUXRYJPufaBuMNlzWJSCV%2FVL%2ByMjXjU%2BgpWgTz7kra5w0VxToJ0rrThan5gecnI1QP5qaUbpTID8x8Po94RSFMAyrUKDx95CgN7hA%2BeDmIL0%2BWr83wflgs9aEzt2TcHryvOl5uxT1%2Fa1yF3CcbEzn2ixNQLDOQueAHRXS3xAfHcrmhh1VJZu%2Fft2Ey95O4vkJ1pXBw%2BH27JNB6dXHbavW6%2B30V3PDb1jqijWCbolpVYJ3Sbf1fCariArf%2BkJKG3DrPyzCF16vIBjqkAWwoBNBkmvStjp9PT5kINGyXwUjoC920x1Ru5zBQwsBPkASqPSmfiAGU1ilS8k2VwVR0hCsu2Skfqo%2F4D2NDH8UPqDvgBngbw7Ay5O%2BFZTMCmkp1Egn5WlNro6lskLqumBmcaPQERW%2F6UZe5XM5jQZtQ1eVF2SV1EPm5eUS7kzXwU8S4vCPurpUQ0YmRpx%2FGL7oXJjVK6JfOIFIGza%2BG%2FnqGXVEY&X-Amz-Signature=ac90a83e199a8c2e180510c2fe45ce1739f7b08d1810045a3fa90972459be2b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test







