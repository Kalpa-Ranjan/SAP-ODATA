



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5WES6LW%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T032554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDWIexnID4Q%2BovQAFUIp2zN57o9gwo5%2FURuoVUlAtw8hAiEAgem4gsxpqOR%2BtUIsxGl7cxVlHsCixvPWpM6n2rLQGrQqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHaV%2BssX8MHcUwJxCrcA78mzztbYtKGXiei8ilBrV8D%2Bh5xg72ePQIlqou0%2FhOxtQ5cHKS%2FDXfLwrX5ZjeaBvwCGQ9CjfARs%2BTuf2xURZnNsBwzUAu1RmGP%2FFcuAxVIcAz6SwPrt64IFkskPmWn4t0SU2Rks9DY7jvXUC3o6xiaPh9yEuqyxlGbaXOnIVisNc0p4U0ZSMEZMvIrhfOO%2BkzRqHGF7HniaokDckC2gMtpskyjLQ%2BOJ6BgBEyEzLCr9yJBbh18dpeZiXwr%2FBx%2BQS%2BMOohpfC%2BXU5F7nKw6uaIpsMz20nV3oFgAfHJnPHrFN9wIZ16Oa6av6uIh%2F0u717HHgY5cE%2F2z78%2FqBx80QZcrRuwEJg8NIubHNnKvZf1cXg5nvKwoDaFg%2F1YzGQTtiAFscoQtxAIsGT2GypMqSzhLvIu6MThwcmV6RgZ%2FIYYuGViIf4q%2Fui%2BBZdALCd6%2Bk9BAJDH3tO1TbQe6NfK0AeA5ggznB%2FKtRTUYFr9hHVDlCR%2FFDq3btaayQ9VgfnvYmYw2BPIQNxUrxjw1TsWchfU%2F2VumISGr%2BxiNAflhw%2BTtV%2FvjnuM0skxLnomr1p%2BomFDGq3%2F03wOaQl81Zg6UVmbeII9Ruou1Vo1TfMoKVkqowFuwnQxzYXHn%2BkWmMP2vzdEGOqUB%2BR17DX8uk5LspsOrCXUW%2F0rVX14JKLcSJiwf%2Fv%2B2L3h2DOXPFKniJ%2BRmYFkYs6oOLPIQ89CLvnIDgBFC6Ge6uFuD6t7%2BL09KcUmQSWFjN9EPKsD02dtFUGbiV96iN9cLj3A3rMlFg2C3tynIraPRA5neA8ISXVypCr51quVmN2Y5LElmFKvqaKLyL4w2cMdOoUnyi5TxYbPZ%2F3w%2BZj9ptkovZV%2Fl&X-Amz-Signature=8dc0aa7996e335744fcd6b7cae2504e5aa35d1dbc97fb8372d606bfc2117f3b3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Y5WES6LW%2F20260618%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260618T032554Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDWIexnID4Q%2BovQAFUIp2zN57o9gwo5%2FURuoVUlAtw8hAiEAgem4gsxpqOR%2BtUIsxGl7cxVlHsCixvPWpM6n2rLQGrQqiAQInP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDKHaV%2BssX8MHcUwJxCrcA78mzztbYtKGXiei8ilBrV8D%2Bh5xg72ePQIlqou0%2FhOxtQ5cHKS%2FDXfLwrX5ZjeaBvwCGQ9CjfARs%2BTuf2xURZnNsBwzUAu1RmGP%2FFcuAxVIcAz6SwPrt64IFkskPmWn4t0SU2Rks9DY7jvXUC3o6xiaPh9yEuqyxlGbaXOnIVisNc0p4U0ZSMEZMvIrhfOO%2BkzRqHGF7HniaokDckC2gMtpskyjLQ%2BOJ6BgBEyEzLCr9yJBbh18dpeZiXwr%2FBx%2BQS%2BMOohpfC%2BXU5F7nKw6uaIpsMz20nV3oFgAfHJnPHrFN9wIZ16Oa6av6uIh%2F0u717HHgY5cE%2F2z78%2FqBx80QZcrRuwEJg8NIubHNnKvZf1cXg5nvKwoDaFg%2F1YzGQTtiAFscoQtxAIsGT2GypMqSzhLvIu6MThwcmV6RgZ%2FIYYuGViIf4q%2Fui%2BBZdALCd6%2Bk9BAJDH3tO1TbQe6NfK0AeA5ggznB%2FKtRTUYFr9hHVDlCR%2FFDq3btaayQ9VgfnvYmYw2BPIQNxUrxjw1TsWchfU%2F2VumISGr%2BxiNAflhw%2BTtV%2FvjnuM0skxLnomr1p%2BomFDGq3%2F03wOaQl81Zg6UVmbeII9Ruou1Vo1TfMoKVkqowFuwnQxzYXHn%2BkWmMP2vzdEGOqUB%2BR17DX8uk5LspsOrCXUW%2F0rVX14JKLcSJiwf%2Fv%2B2L3h2DOXPFKniJ%2BRmYFkYs6oOLPIQ89CLvnIDgBFC6Ge6uFuD6t7%2BL09KcUmQSWFjN9EPKsD02dtFUGbiV96iN9cLj3A3rMlFg2C3tynIraPRA5neA8ISXVypCr51quVmN2Y5LElmFKvqaKLyL4w2cMdOoUnyi5TxYbPZ%2F3w%2BZj9ptkovZV%2Fl&X-Amz-Signature=1619eaba47ed228164f4f270d3b2f3efd40ac1813a29b27837891dddb38836f7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







