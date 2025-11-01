



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNC77POK%2F20251101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251101T122744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQD8qn4X%2BgxkCE2OAduiQV43x5HYSn80%2B21pge4BeFLNWAIhAKxiLM%2FVyB3xQg1ks8K95q3Ho8e3YksufdKyFTr0LAQnKv8DCCgQABoMNjM3NDIzMTgzODA1IgwUPKsLKyimeOw9gdcq3AMh%2BmvI7I2%2FBhivByskobWfg65EAM%2Fhbm6Bz9ml7MjtoWNXWiDhbU4AhnwPVXROEm3lh3Jk9PihR8pyyn5Ql9vbpf2as5i37o5xuIZAwPQWDYIlUogCIrhLGnzsHNxtOxsyMKxSXwBsEXgOkCOlMIDPM%2BBcXNuNjENuxxVSoyYwo8f%2Bn6gCLQ4fjdu%2Bu71HC8tgcN8y%2FvwqrCfN%2FspRtFBXPjeRBmucu8nyLaiOhERwOIE20tcgmgWm%2Bytp2dCHCIRk%2F4gl8WiTxcqYTX1QCR0gE%2F5nW%2FACV%2BJg%2FyZ7qY0tAkFh8VVZq%2B8JcLTUJNgvZENiWe2yAxa8Bc%2BvjgwshzTCeA8YNEhNlvfNAu25icwYN2R3CE83Vy1Ahj0RKQQhsjK7DYkYZ%2FwdXaQDBlc8R9of%2Fnl7yVWb232EERFb2%2FUihoyf%2B4mda1lSGeOpKVeSNBP7CJDY9Yn1O%2FABRVQeWO%2FSyTEfIr7u2bbKfcTRh6V9xl2Vq91Wq3tYpBo9Ap0cze424HD%2F6fB3q9S923YBtrQ0XHNK9Wlm5gpvwDiM6Ve1Dmj%2FHYXxYRTfpzeR09Y8D6KG8tlXPMXO3lMjTlTWzP9gOoGFc1SyWVTe7kmOOjnpCfP50o4WPwM4CMRV8jCg6JbIBjqkAdqK5Wlc1TT3rrxFzeUZqLZ7Z6b9OAnsoNTkdRj6R2SNP10SnBtWC7NxXlq%2Buc3e%2FtxvVwoK%2FymTLI4RwV0t42leapO27p3JIeijWBYJjfKiUCLFurepusIRNmOGmK5WxfxBH7sSh4wTqN%2BXCWGBFFUkMPbZNqarsdXGXh5SGqN75dwufAaI8nA2ruNRgmiB2dxZkIIWtPA5732bw48dSplIfc4I&X-Amz-Signature=779128025ea7ddb17cf52e4859279322a387b564359c9a2c9bb13c06e9d6edf5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WNC77POK%2F20251101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251101T122744Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGAaCXVzLXdlc3QtMiJIMEYCIQD8qn4X%2BgxkCE2OAduiQV43x5HYSn80%2B21pge4BeFLNWAIhAKxiLM%2FVyB3xQg1ks8K95q3Ho8e3YksufdKyFTr0LAQnKv8DCCgQABoMNjM3NDIzMTgzODA1IgwUPKsLKyimeOw9gdcq3AMh%2BmvI7I2%2FBhivByskobWfg65EAM%2Fhbm6Bz9ml7MjtoWNXWiDhbU4AhnwPVXROEm3lh3Jk9PihR8pyyn5Ql9vbpf2as5i37o5xuIZAwPQWDYIlUogCIrhLGnzsHNxtOxsyMKxSXwBsEXgOkCOlMIDPM%2BBcXNuNjENuxxVSoyYwo8f%2Bn6gCLQ4fjdu%2Bu71HC8tgcN8y%2FvwqrCfN%2FspRtFBXPjeRBmucu8nyLaiOhERwOIE20tcgmgWm%2Bytp2dCHCIRk%2F4gl8WiTxcqYTX1QCR0gE%2F5nW%2FACV%2BJg%2FyZ7qY0tAkFh8VVZq%2B8JcLTUJNgvZENiWe2yAxa8Bc%2BvjgwshzTCeA8YNEhNlvfNAu25icwYN2R3CE83Vy1Ahj0RKQQhsjK7DYkYZ%2FwdXaQDBlc8R9of%2Fnl7yVWb232EERFb2%2FUihoyf%2B4mda1lSGeOpKVeSNBP7CJDY9Yn1O%2FABRVQeWO%2FSyTEfIr7u2bbKfcTRh6V9xl2Vq91Wq3tYpBo9Ap0cze424HD%2F6fB3q9S923YBtrQ0XHNK9Wlm5gpvwDiM6Ve1Dmj%2FHYXxYRTfpzeR09Y8D6KG8tlXPMXO3lMjTlTWzP9gOoGFc1SyWVTe7kmOOjnpCfP50o4WPwM4CMRV8jCg6JbIBjqkAdqK5Wlc1TT3rrxFzeUZqLZ7Z6b9OAnsoNTkdRj6R2SNP10SnBtWC7NxXlq%2Buc3e%2FtxvVwoK%2FymTLI4RwV0t42leapO27p3JIeijWBYJjfKiUCLFurepusIRNmOGmK5WxfxBH7sSh4wTqN%2BXCWGBFFUkMPbZNqarsdXGXh5SGqN75dwufAaI8nA2ruNRgmiB2dxZkIIWtPA5732bw48dSplIfc4I&X-Amz-Signature=2e7deeabeaf096ae5a8b922c9de0a9296ee344ab0fc777302978e3f1e5858584&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







