



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U64CHAOB%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T205030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQDcGkQkvKbGpzaldf%2BGiBksBH9lAjo9ETSkHp0jPPHF3QIhAI2JGe3vLn3amPALqy8fRjz%2FKAWgQl3%2B4beFCZGhqlX2Kv8DCEQQABoMNjM3NDIzMTgzODA1IgzPlVsYfZkWcLXwyVUq3APr2xto%2BLHBRIpDuKN5gf3q%2FYyG15z6kYd8elpptjDtuk9HGf%2FyiQWL1tie%2BbFEl1sSZwQ3i3pwKXZMd9hJNOwG%2FbesF8rGEai5KJN4%2FCPkT00HTwrXv0W29XV7U5XMcESbkSuNfjo8qNyWFrPS1wdMRt6E6gqqRNYGpnEAxT18Yc1ny%2BEyIrt64dJbiwhwkracNtmMqV6Ghyeu4i6pLL%2FGqwvYcRdvb0CJ79LN3d%2BD9%2FPCJymzZSlabNWPTFV9zHfaobUPIcCHU4hVLdmmFXXZQt1%2FEP4InsfmVdCI3QXqnl7mRzL57Ltva4plAHrP3c3WZ54UXcVpY4xHZh9T3DRaR45WxIbWhAvHXR2BTWGpOEMDKqd8xdoGLfsEvRN0py0npKOEKMHqXR71vRRFOIlxdkMZWuGuMofjif%2BsWKalZbUz1C9KdjPGo9Gt9dEvWeCakGwxorVWAyMlFWVj5qawmTUml9d72BEufw0WMKy55%2FZV%2BJvV7Zk9OmCK793TH4%2FxKjLaM1Yr%2B5D4OrLKHC0as%2FJHDJeJgmUURymFb5xQYj6fArwwxlXqP7Gzj%2BATh8iPe1ntbO5JTp500dKV1%2BI370KOSdATwoLDJVXuRjBUjPACgn5jLYY6ezQDbjCDgILRBjqkAat6Tx5%2BPHctF9%2FhEo4WIgu4L5dCjIVzE9EBTyFqsfoYh%2FIJ3J7lZEy1e8Ka1x5Bq7eZzc30KRQNBfw%2FTn8riHd3CU%2Bnxf8zHG2L81GfgaEEg3Swz1qg9V1niK6GPpj4W06pnI3g3VyVsdd1n2ob9El5SJL5JauB26VBb6nJKp2oU3dO%2FUHs%2Fy5tH4UxR4tPfVT1xE832BTI4Ce%2FL7xUs5KHhHTb&X-Amz-Signature=ae10c96495f53b34cdd092eda49933e59ec05e6dc6a8bfd1dbe9c0b688721ee6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466U64CHAOB%2F20260603%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260603T205030Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEHwaCXVzLXdlc3QtMiJIMEYCIQDcGkQkvKbGpzaldf%2BGiBksBH9lAjo9ETSkHp0jPPHF3QIhAI2JGe3vLn3amPALqy8fRjz%2FKAWgQl3%2B4beFCZGhqlX2Kv8DCEQQABoMNjM3NDIzMTgzODA1IgzPlVsYfZkWcLXwyVUq3APr2xto%2BLHBRIpDuKN5gf3q%2FYyG15z6kYd8elpptjDtuk9HGf%2FyiQWL1tie%2BbFEl1sSZwQ3i3pwKXZMd9hJNOwG%2FbesF8rGEai5KJN4%2FCPkT00HTwrXv0W29XV7U5XMcESbkSuNfjo8qNyWFrPS1wdMRt6E6gqqRNYGpnEAxT18Yc1ny%2BEyIrt64dJbiwhwkracNtmMqV6Ghyeu4i6pLL%2FGqwvYcRdvb0CJ79LN3d%2BD9%2FPCJymzZSlabNWPTFV9zHfaobUPIcCHU4hVLdmmFXXZQt1%2FEP4InsfmVdCI3QXqnl7mRzL57Ltva4plAHrP3c3WZ54UXcVpY4xHZh9T3DRaR45WxIbWhAvHXR2BTWGpOEMDKqd8xdoGLfsEvRN0py0npKOEKMHqXR71vRRFOIlxdkMZWuGuMofjif%2BsWKalZbUz1C9KdjPGo9Gt9dEvWeCakGwxorVWAyMlFWVj5qawmTUml9d72BEufw0WMKy55%2FZV%2BJvV7Zk9OmCK793TH4%2FxKjLaM1Yr%2B5D4OrLKHC0as%2FJHDJeJgmUURymFb5xQYj6fArwwxlXqP7Gzj%2BATh8iPe1ntbO5JTp500dKV1%2BI370KOSdATwoLDJVXuRjBUjPACgn5jLYY6ezQDbjCDgILRBjqkAat6Tx5%2BPHctF9%2FhEo4WIgu4L5dCjIVzE9EBTyFqsfoYh%2FIJ3J7lZEy1e8Ka1x5Bq7eZzc30KRQNBfw%2FTn8riHd3CU%2Bnxf8zHG2L81GfgaEEg3Swz1qg9V1niK6GPpj4W06pnI3g3VyVsdd1n2ob9El5SJL5JauB26VBb6nJKp2oU3dO%2FUHs%2Fy5tH4UxR4tPfVT1xE832BTI4Ce%2FL7xUs5KHhHTb&X-Amz-Signature=f567ee0d05f28cee85a8f0bd55a42e9b7fc77956be8528f6c4d72473951f7ccc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







