



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOXIFYSJ%2F20260611%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260611T201336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIF%2BRno3%2FUrHzuTCh05gekYKaxGtGOorUmMyuChaUKu4HAiB3FdmpAOlP%2Bp9FNQxnFmplne5ZHbDcfku3TvxAyPXUeyr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIMkj2ENbQVH1YjobzZKtwDnnBSro7OGtj4ONRYkIBv8hQo%2BtEtsxAoNlec6%2Fa3zfFCmp2CqFOD7qHrU6cgdi7gsYnpntgB572BJiMJotFTPwHm%2FvbiE8TtKfbK3Zi%2BL9p6gCTqTpZ1R1yyU1yHA6VL7VJ53%2FQ8KJKh9esWhf400Hwo1S6Wov6XQIJl9M0aR6tloV58J6SiPPQdrUpHbNYOHVJ0tsr400svignUMdM3P6PY8yJakn6rWNeAYHrSOb79I6DKYf62C1FggAf5RVDum8jopfoS9wvMoLdJpSZfLd2MoGkDpbpmExZJKbIF0OarFkI%2BQ%2BSkMcSMunvVcAnP26YjbW6IK2RuIKyQbGTmaZCs2K1wvMc5cyfqMl2%2BXTEsSAPC2B0AM9PomPsQoZ1IsCWyKDslZ0%2FyX%2BZ%2FRdRGnLeWBWDMc8QCimFCTynUQUmGIKckCh1u5vu5D13UD7AKRSn0Pl6gCWDMg%2FPTRvCOgPTPZ0x8al9889CGuSsK0Tw7VmwRG4UpvdT6sZ87z%2FleZPIZhuRYVkOURzcw0yHlXL1BjaPN8NB08YNnEC70U0ssHiaCDaPS0k7oScdpn%2FFqo9FiBiTPh%2BsX7tf%2BnnhFJl%2FwiNDN57fSW0FhXTevkBugVzkDCXtefxN7Cdkw6Kqs0QY6pgFpUKU2LU6L5iN7orEy441ue0h8cbcK7WhbFqrSdClrjdpNClDuQlNBSIpFlcQl%2FwX8Pmwr21SOOSPPFNlPlscbgSeOJ7amYUAPk2pGeFArAUtfPHyoSwrdD%2FDsNOz3mGnJG6PPwA8S6LrtgN7QjXD1NVnhOg2pTaEZJtZuUQUv5WSIFvutRXAsrCtQr56wQNfg7FgmWJpLwPXom6HHmSjz3AYZh8rw&X-Amz-Signature=2c07c7ec123f31e73790b35ab10701902073831a14a69939ce5ac35575e58a88&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZOXIFYSJ%2F20260611%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260611T201336Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDwaCXVzLXdlc3QtMiJGMEQCIF%2BRno3%2FUrHzuTCh05gekYKaxGtGOorUmMyuChaUKu4HAiB3FdmpAOlP%2Bp9FNQxnFmplne5ZHbDcfku3TvxAyPXUeyr%2FAwgFEAAaDDYzNzQyMzE4MzgwNSIMkj2ENbQVH1YjobzZKtwDnnBSro7OGtj4ONRYkIBv8hQo%2BtEtsxAoNlec6%2Fa3zfFCmp2CqFOD7qHrU6cgdi7gsYnpntgB572BJiMJotFTPwHm%2FvbiE8TtKfbK3Zi%2BL9p6gCTqTpZ1R1yyU1yHA6VL7VJ53%2FQ8KJKh9esWhf400Hwo1S6Wov6XQIJl9M0aR6tloV58J6SiPPQdrUpHbNYOHVJ0tsr400svignUMdM3P6PY8yJakn6rWNeAYHrSOb79I6DKYf62C1FggAf5RVDum8jopfoS9wvMoLdJpSZfLd2MoGkDpbpmExZJKbIF0OarFkI%2BQ%2BSkMcSMunvVcAnP26YjbW6IK2RuIKyQbGTmaZCs2K1wvMc5cyfqMl2%2BXTEsSAPC2B0AM9PomPsQoZ1IsCWyKDslZ0%2FyX%2BZ%2FRdRGnLeWBWDMc8QCimFCTynUQUmGIKckCh1u5vu5D13UD7AKRSn0Pl6gCWDMg%2FPTRvCOgPTPZ0x8al9889CGuSsK0Tw7VmwRG4UpvdT6sZ87z%2FleZPIZhuRYVkOURzcw0yHlXL1BjaPN8NB08YNnEC70U0ssHiaCDaPS0k7oScdpn%2FFqo9FiBiTPh%2BsX7tf%2BnnhFJl%2FwiNDN57fSW0FhXTevkBugVzkDCXtefxN7Cdkw6Kqs0QY6pgFpUKU2LU6L5iN7orEy441ue0h8cbcK7WhbFqrSdClrjdpNClDuQlNBSIpFlcQl%2FwX8Pmwr21SOOSPPFNlPlscbgSeOJ7amYUAPk2pGeFArAUtfPHyoSwrdD%2FDsNOz3mGnJG6PPwA8S6LrtgN7QjXD1NVnhOg2pTaEZJtZuUQUv5WSIFvutRXAsrCtQr56wQNfg7FgmWJpLwPXom6HHmSjz3AYZh8rw&X-Amz-Signature=3fbdf2077ea12676fdacda79302c9163d1fdd0e87919b4c58d6a525d122706cf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







