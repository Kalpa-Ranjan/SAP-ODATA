



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZYGQKZ6%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T190224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJIMEYCIQDVgQ1Bv2WvjjvcyAdKB5x1GL6PjWDXVschO%2F0A0vLcFwIhAND%2BoSSGkdYRkiXeS6zwzAfndYrLCVWdaeDFdo%2BHxQqfKv8DCDkQABoMNjM3NDIzMTgzODA1IgwrMJcZkgNqdYaTe9Uq3ANjw%2BVQboM%2FhhecYh5xNAvAAO7pSrdONlVw%2FNhYAANAmIzbmIXpBySVzhObJRwa909EdSuUSzVroUUf6upF%2FzsUygwg2bvuQsUWDB7urPTCelYGLQX1gtkb%2B3I8m9UxlnUXqGv4l50l%2BlI7eeN9ZHRpUfjqvhRwR49XCdxG%2BU3D6F8yWvcEiPjtbiubj%2FW0hNcvQsyjKnDVlZX%2FdaWVFsC%2B3fz63AxYTipV3GpofVSDrBPBTlEoxnK6PSNi16dXN5KDLHEBz5YYgnnKecdBIEuhwsVX17A7gthj4coyKmcq%2FsPWfmEQ%2Bmus4XXB4FvruDr8FipuWw5dwZfYv3uH%2BvBJDvPXgyH5HrUjgfiyy%2Basnkap9vXcLq36k%2BJaFTmVX%2B593Y25MZHfuFBLchBW2AzOUb60JdcV2rB2A%2BitY%2BoLQWTPqKn8WVa7M9uNQgs8MRe8PKk8vWDrndywU7Rwn5CkbvSJiAy9SsA9TrKMhAS%2BvHLlkbX34j8C%2FzMFWTEYLr8MB5lN4eJl%2FAJTSVqvXCPk5IlzAFLH5aTB74kmsiIdwHyS3IUur9wNGUY3Aij9dvKiGzFPdgerkZkTBRQKDFgLFLWRri1S8TjvMHHUIJf0pkFcRFn1HFVJhXCiNTCA65jTBjqkARVZQqxV4FjJhYf7csZd40r4cryBn%2BPLMzzg66mqiSdi%2BJkhL4tleyrEGsy3f7Z1DYxM7cIO2paHsaGil6IcKWYvWIUQJ%2B166MWzG88SjywBWOWGPbPDpaYaAe5%2BUeI0v3YBxEXdN8ga7eVgSMSpTxTGp6AsDBBkLDcn%2FLJIBpPlNVc34hBHrs56LY01ISzQ7nKvOlh5TtqAqXxfdZ5cyx0nd3wB&X-Amz-Signature=fbc042bf04c746bd8309176917a20bce8bbcd4a314a01a2cd6f7704450f259e0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZYGQKZ6%2F20260726%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260726T190224Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHEaCXVzLXdlc3QtMiJIMEYCIQDVgQ1Bv2WvjjvcyAdKB5x1GL6PjWDXVschO%2F0A0vLcFwIhAND%2BoSSGkdYRkiXeS6zwzAfndYrLCVWdaeDFdo%2BHxQqfKv8DCDkQABoMNjM3NDIzMTgzODA1IgwrMJcZkgNqdYaTe9Uq3ANjw%2BVQboM%2FhhecYh5xNAvAAO7pSrdONlVw%2FNhYAANAmIzbmIXpBySVzhObJRwa909EdSuUSzVroUUf6upF%2FzsUygwg2bvuQsUWDB7urPTCelYGLQX1gtkb%2B3I8m9UxlnUXqGv4l50l%2BlI7eeN9ZHRpUfjqvhRwR49XCdxG%2BU3D6F8yWvcEiPjtbiubj%2FW0hNcvQsyjKnDVlZX%2FdaWVFsC%2B3fz63AxYTipV3GpofVSDrBPBTlEoxnK6PSNi16dXN5KDLHEBz5YYgnnKecdBIEuhwsVX17A7gthj4coyKmcq%2FsPWfmEQ%2Bmus4XXB4FvruDr8FipuWw5dwZfYv3uH%2BvBJDvPXgyH5HrUjgfiyy%2Basnkap9vXcLq36k%2BJaFTmVX%2B593Y25MZHfuFBLchBW2AzOUb60JdcV2rB2A%2BitY%2BoLQWTPqKn8WVa7M9uNQgs8MRe8PKk8vWDrndywU7Rwn5CkbvSJiAy9SsA9TrKMhAS%2BvHLlkbX34j8C%2FzMFWTEYLr8MB5lN4eJl%2FAJTSVqvXCPk5IlzAFLH5aTB74kmsiIdwHyS3IUur9wNGUY3Aij9dvKiGzFPdgerkZkTBRQKDFgLFLWRri1S8TjvMHHUIJf0pkFcRFn1HFVJhXCiNTCA65jTBjqkARVZQqxV4FjJhYf7csZd40r4cryBn%2BPLMzzg66mqiSdi%2BJkhL4tleyrEGsy3f7Z1DYxM7cIO2paHsaGil6IcKWYvWIUQJ%2B166MWzG88SjywBWOWGPbPDpaYaAe5%2BUeI0v3YBxEXdN8ga7eVgSMSpTxTGp6AsDBBkLDcn%2FLJIBpPlNVc34hBHrs56LY01ISzQ7nKvOlh5TtqAqXxfdZ5cyx0nd3wB&X-Amz-Signature=4545dfc655db618bd81f64384dfe888b1926385e1f2ea807962cbfe751fa4da8&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







