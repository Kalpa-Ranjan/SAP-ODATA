



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZGPMJWU%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T130006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIEpJMBt0LoYYKm%2FnQDlm1itJZF%2F4BQDmYyBAhMptQQktAiEAmWLu%2BQgleFeoiHwOU8MxtotlVZUxx6IZwyy9bcQXT1Eq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDBU7Zi18dx%2Fa22wS%2FyrcA98e1y29Trewai0EGLcyd20f6rjg55sRNlrggnEW7Cjc3KgeM4qC90rJ%2BNusLEvzrr8zuX3c0J2km4DsBVKoaTLSSTl%2B%2BPYashd8Sl3FC8pioGypOvmAVRgaXUvsiBGBcRrIGjb8qKz7Xkx10GC4kXIWXLVUb47%2BT%2BVW6h42T0Mve8nK6jGdx8YBm643%2B%2BeBxdibPKE60gxFme%2FstnwkbvO5ypWnDQHMHdFJOLiMdL%2BII%2FTE2bya1S71ETHmr6EveCf6knbmrVNG2k5Q2Hvgd5fn39EnEx5WWMfsWV4EhUVEPnh3LupGZ%2FPReUzMIShUmR0Znr4dkyxFdykaa6B1opp%2FHysg0JfQc3ZknnSYLY1J5Y93%2FziwnAFdtFk3gXGWhfz785LhIXViMp81M%2BdvwFKEdRp%2Fs3YSMxwHuMiF6t3ZUPWzVCb9riJnTbM1WRrUIE4dT3No66DaHmmMZ%2FisnNwImaFaxG3TlFnwIvFJQlwZu8ZIy3O8VG9U5m%2Fqa0Jea1cQLTsKrJi%2FXhX4kJyuH1Er3c5P4MHMV56SzJsQYiTsptbxNdRaZsRyiBdhCYOQN3RSPuoEJpy%2B9aSQYQ%2FrLZ7Ht8FVmadqyd9awo86Luc0I5CHIFDxNtwQjLkIMJef6s0GOqUBfmCEhaY2R%2BOgSjs6lrPUUFEG20yyLHZbwKJXiO1a9xyPTqkZtCLQvUeyErIxtKMn3f4sisGwDDu6c0PavsPYhEGqwvQa2R0jtGivBrraPjRoAga63pVL050amNGXurmYcj7IcRBMERmqWc%2BThNSbtgqZWjWSixSmtw5x4akZSVW0Hp6lq7hKhzN1evMr8OdkYIsu7WHrnHCaCuzIKRPv3BMsXYjS&X-Amz-Signature=63699ab045285f60d6652c365508dd6b4b3975d9221085290d8447a19ffb5d0e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QZGPMJWU%2F20260318%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260318T130006Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJHMEUCIEpJMBt0LoYYKm%2FnQDlm1itJZF%2F4BQDmYyBAhMptQQktAiEAmWLu%2BQgleFeoiHwOU8MxtotlVZUxx6IZwyy9bcQXT1Eq%2FwMIBRAAGgw2Mzc0MjMxODM4MDUiDBU7Zi18dx%2Fa22wS%2FyrcA98e1y29Trewai0EGLcyd20f6rjg55sRNlrggnEW7Cjc3KgeM4qC90rJ%2BNusLEvzrr8zuX3c0J2km4DsBVKoaTLSSTl%2B%2BPYashd8Sl3FC8pioGypOvmAVRgaXUvsiBGBcRrIGjb8qKz7Xkx10GC4kXIWXLVUb47%2BT%2BVW6h42T0Mve8nK6jGdx8YBm643%2B%2BeBxdibPKE60gxFme%2FstnwkbvO5ypWnDQHMHdFJOLiMdL%2BII%2FTE2bya1S71ETHmr6EveCf6knbmrVNG2k5Q2Hvgd5fn39EnEx5WWMfsWV4EhUVEPnh3LupGZ%2FPReUzMIShUmR0Znr4dkyxFdykaa6B1opp%2FHysg0JfQc3ZknnSYLY1J5Y93%2FziwnAFdtFk3gXGWhfz785LhIXViMp81M%2BdvwFKEdRp%2Fs3YSMxwHuMiF6t3ZUPWzVCb9riJnTbM1WRrUIE4dT3No66DaHmmMZ%2FisnNwImaFaxG3TlFnwIvFJQlwZu8ZIy3O8VG9U5m%2Fqa0Jea1cQLTsKrJi%2FXhX4kJyuH1Er3c5P4MHMV56SzJsQYiTsptbxNdRaZsRyiBdhCYOQN3RSPuoEJpy%2B9aSQYQ%2FrLZ7Ht8FVmadqyd9awo86Luc0I5CHIFDxNtwQjLkIMJef6s0GOqUBfmCEhaY2R%2BOgSjs6lrPUUFEG20yyLHZbwKJXiO1a9xyPTqkZtCLQvUeyErIxtKMn3f4sisGwDDu6c0PavsPYhEGqwvQa2R0jtGivBrraPjRoAga63pVL050amNGXurmYcj7IcRBMERmqWc%2BThNSbtgqZWjWSixSmtw5x4akZSVW0Hp6lq7hKhzN1evMr8OdkYIsu7WHrnHCaCuzIKRPv3BMsXYjS&X-Amz-Signature=26bd7ed0879cccc1e19aa5f9d6a7d9f07831f4e7205e44460b22e5bdd60e7994&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







