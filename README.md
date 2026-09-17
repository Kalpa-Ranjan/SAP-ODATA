



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5IYZBNY%2F20260917%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260917T061343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDh658uv4A9%2Fq%2FuZ390HofsWrnEQOT3GpoIqXBtmuEeOwIgDYJiGK8qpP0Rwl5yJrqs4bC%2FQ1l8j1vOvii5bZ1ZbUQq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJmuJ0nyVz85fr8N%2FSrcA12nno87F6W0R05LE9q8RpgU3uxcRUairFHGUU79NWlN8BGSiDo3EnLM3QltBBSqjU%2FvkUXU%2FEF89lswMtungeBntaOuBsuqgXXIUtjzYpLhS7i84phHqD5SV%2FWpf618syDm5XueUg%2B9gc8SZmTIGL7xY4CfIrdgs11uG%2FDpIsC2FKYFNL21UuzKaDIyrgs6K%2Fv1J8RyfU3pAM5%2FLpMbm3cv3%2BpnrZ5d01r6VlqiOXzBK5IdebGQtyrbkkeIVAw3CbOhC%2BE17666tNIN5suF65cEmwIZl3qEktUN7ecWFf6zhZw2MWH%2BMYDaZeHTX0zfOrrj4TLIe48d4LqAeMHnViXvJszzCEMfRnxqSixy8u%2BiAFenIO5lYnl%2F0x83zEMRjOEXHuLP%2BgdHcDE%2BZMJtzgjzGLxMu07T39QPZNxw5ZFe8cxSY5c%2BSs1wEA7BNYH8iQjXreW1%2BCDU65TDyVDKuqX35s2pzJkLpaW7gTpTUtWw9nJiK9rzvFd2VK%2BG5XKHLSdwEYzpsYb35Y9%2BXpBCZyajMq7hc2JsyszEDsSM4Q%2BwV%2FJY58re2bApR8PBAN4oR1eOn5x9Ed4yAtln6WwHPxnebpfTzRW5%2BYjcmHS8O5ADzcO3dotwlScfpDI9MIXmrdUGOqUBSvrqPTYDjLqNc0OaKskC59qZaAQjNQNSrKLMUXxFasFsFUPTwS0n3pFY1dBoTIONTpaCv43daAVXpCV638DuvG8x4DDqTqGny5YcbBtrW4Yre%2Bbe9ytw0qHH00fyngOHPWtF0IIuXz2%2FiyZy3FBc%2FCZTTxYko5z%2FgBI6yIJlwr%2Fk2Ldq%2Bgigt%2FnvXfQGHKaj9vZ8nX7Q2Xyh8%2B%2Fh4bvDUDFzLr7a&X-Amz-Signature=08b006956201d77ec6251d29053827aa73543c28ba1f501d2be781e05a28597d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466T5IYZBNY%2F20260917%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260917T061343Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF0aCXVzLXdlc3QtMiJHMEUCIQDh658uv4A9%2Fq%2FuZ390HofsWrnEQOT3GpoIqXBtmuEeOwIgDYJiGK8qpP0Rwl5yJrqs4bC%2FQ1l8j1vOvii5bZ1ZbUQq%2FwMIJhAAGgw2Mzc0MjMxODM4MDUiDJmuJ0nyVz85fr8N%2FSrcA12nno87F6W0R05LE9q8RpgU3uxcRUairFHGUU79NWlN8BGSiDo3EnLM3QltBBSqjU%2FvkUXU%2FEF89lswMtungeBntaOuBsuqgXXIUtjzYpLhS7i84phHqD5SV%2FWpf618syDm5XueUg%2B9gc8SZmTIGL7xY4CfIrdgs11uG%2FDpIsC2FKYFNL21UuzKaDIyrgs6K%2Fv1J8RyfU3pAM5%2FLpMbm3cv3%2BpnrZ5d01r6VlqiOXzBK5IdebGQtyrbkkeIVAw3CbOhC%2BE17666tNIN5suF65cEmwIZl3qEktUN7ecWFf6zhZw2MWH%2BMYDaZeHTX0zfOrrj4TLIe48d4LqAeMHnViXvJszzCEMfRnxqSixy8u%2BiAFenIO5lYnl%2F0x83zEMRjOEXHuLP%2BgdHcDE%2BZMJtzgjzGLxMu07T39QPZNxw5ZFe8cxSY5c%2BSs1wEA7BNYH8iQjXreW1%2BCDU65TDyVDKuqX35s2pzJkLpaW7gTpTUtWw9nJiK9rzvFd2VK%2BG5XKHLSdwEYzpsYb35Y9%2BXpBCZyajMq7hc2JsyszEDsSM4Q%2BwV%2FJY58re2bApR8PBAN4oR1eOn5x9Ed4yAtln6WwHPxnebpfTzRW5%2BYjcmHS8O5ADzcO3dotwlScfpDI9MIXmrdUGOqUBSvrqPTYDjLqNc0OaKskC59qZaAQjNQNSrKLMUXxFasFsFUPTwS0n3pFY1dBoTIONTpaCv43daAVXpCV638DuvG8x4DDqTqGny5YcbBtrW4Yre%2Bbe9ytw0qHH00fyngOHPWtF0IIuXz2%2FiyZy3FBc%2FCZTTxYko5z%2FgBI6yIJlwr%2Fk2Ldq%2Bgigt%2FnvXfQGHKaj9vZ8nX7Q2Xyh8%2B%2Fh4bvDUDFzLr7a&X-Amz-Signature=9449e4f07bc9954c8b56f2f76046d38bf528f4a810261c6d2e3d559473f8c25a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







