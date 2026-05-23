



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFQYCM5E%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T023512Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIANna1qTnpHOEdc0N2J8dOrJnmBhw7bow2K2LKAc6pAwAiEAlFtg1%2FixT%2F5AmE4usz9odvLGPJBalLLbdfHEDQZ5iXYq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDJ3GShTb2cfUQ8zjdircA4y4QRYsdS6Xb4Qi%2BKa9pvk2WTRNrDkNaTPsyi0LB6sbpYHvs09YhLhukbjWi1f88TwVAUD1pW9bfel%2BgpBpZlODQwgGA5QrtY%2FNOMnzGme23eZJi0QwC5oPx8gnkplysvfF7e9XA%2BlMa0I9%2FnfnJrPXGgPb7iiGz%2FWflecS9Zl2REMHGHfKUgSO%2F%2B%2Fi9BRzdFxEMnPeUKaQtcrOHGkqrJzjkhjA1iIQ%2BjjhlBTxIyVGMLsmWVY%2FPWpN%2B9zNXH8LVOl13nLiBI7QhGOVMixjjt2l66Pmbh%2BRc5kXhJxJcRC7182SOGH7p5Obl%2FEBti3UzsRdMybbmtGvQfNFisjbEBflVUwk3PgSTO5bP5wr7265fJXDRm0pvhUDoSh1%2FUtJ1KSrpTPOZc7aAFo9i%2Fzo%2FpcmsHbgJDMRm00M84dZVUlzbRt8riarNW9O964CKy9339RWTZVQ1U6IdIofa1ul9rEL6B%2BHbhYmOG7DC8MBQYHxqiqPv%2FmsUAYLbCYGnsJgNCd3sia%2F22QOHBv%2BMgxZh%2Br5gz274drDQyTbqcqM5ZB6GdctXyD9dKrnzHD1QDSLd1W%2Fw7GCSlGTPPNaFnk9RQRm%2FpYZ2uGhpn3WpeqdECnbZtyet8zpkNCYIv7HMKn8w9AGOqUBYiE4nyFbS8Na1Q0c74AjNkwMLHnT6iZOhrehBeCNzjRdHhcvW0456bRKpnPv7%2FB0bposFwu3BrHaY2MOVz26D1KZD6ZZCAeIRgoOPozK6nvk%2BTW%2BqOU8GKdZN%2BZGnQT89YQ8ZmRryWO1dxr3ge9d1Rbdfm2k1u3sMNgIQne2BVS2BFBLxvHPgpvDiaeL9P8jwYel0x1%2BPh9ZYPACDH3qFB4nkNuE&X-Amz-Signature=72c1d8ed3465cdecbf27c0cd4d31f0f8e0d1d08a23c9aa9deaec2e097d91d427&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QFQYCM5E%2F20260523%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260523T023513Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEGEaCXVzLXdlc3QtMiJHMEUCIANna1qTnpHOEdc0N2J8dOrJnmBhw7bow2K2LKAc6pAwAiEAlFtg1%2FixT%2F5AmE4usz9odvLGPJBalLLbdfHEDQZ5iXYq%2FwMIKhAAGgw2Mzc0MjMxODM4MDUiDJ3GShTb2cfUQ8zjdircA4y4QRYsdS6Xb4Qi%2BKa9pvk2WTRNrDkNaTPsyi0LB6sbpYHvs09YhLhukbjWi1f88TwVAUD1pW9bfel%2BgpBpZlODQwgGA5QrtY%2FNOMnzGme23eZJi0QwC5oPx8gnkplysvfF7e9XA%2BlMa0I9%2FnfnJrPXGgPb7iiGz%2FWflecS9Zl2REMHGHfKUgSO%2F%2B%2Fi9BRzdFxEMnPeUKaQtcrOHGkqrJzjkhjA1iIQ%2BjjhlBTxIyVGMLsmWVY%2FPWpN%2B9zNXH8LVOl13nLiBI7QhGOVMixjjt2l66Pmbh%2BRc5kXhJxJcRC7182SOGH7p5Obl%2FEBti3UzsRdMybbmtGvQfNFisjbEBflVUwk3PgSTO5bP5wr7265fJXDRm0pvhUDoSh1%2FUtJ1KSrpTPOZc7aAFo9i%2Fzo%2FpcmsHbgJDMRm00M84dZVUlzbRt8riarNW9O964CKy9339RWTZVQ1U6IdIofa1ul9rEL6B%2BHbhYmOG7DC8MBQYHxqiqPv%2FmsUAYLbCYGnsJgNCd3sia%2F22QOHBv%2BMgxZh%2Br5gz274drDQyTbqcqM5ZB6GdctXyD9dKrnzHD1QDSLd1W%2Fw7GCSlGTPPNaFnk9RQRm%2FpYZ2uGhpn3WpeqdECnbZtyet8zpkNCYIv7HMKn8w9AGOqUBYiE4nyFbS8Na1Q0c74AjNkwMLHnT6iZOhrehBeCNzjRdHhcvW0456bRKpnPv7%2FB0bposFwu3BrHaY2MOVz26D1KZD6ZZCAeIRgoOPozK6nvk%2BTW%2BqOU8GKdZN%2BZGnQT89YQ8ZmRryWO1dxr3ge9d1Rbdfm2k1u3sMNgIQne2BVS2BFBLxvHPgpvDiaeL9P8jwYel0x1%2BPh9ZYPACDH3qFB4nkNuE&X-Amz-Signature=dde9de96e990c297c01011c78b8b18ab30dcf8a25c45a4a04579f53db4fa2d2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







