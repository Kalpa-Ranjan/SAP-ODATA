



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656RMAUFI%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T020641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCYsN8KdBvQvzSiaKhxU7BB8Y3f55OSu9RmKjLUzfnMOQIgY1%2FsLhPLeznM8jeku0915zdPG0Goo6FJNjYL9tm%2FRegqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJJHBJwulP39oV12EyrcA%2BOClf5UzZ6HJGfDEVlDj3jp%2BL%2BWnkngwUt5E0QdQH4gn6QadSb12C%2FZPFmd0Lv3OFM%2FXoFIIWXWq1aK62FhPo7GPe%2FXoEUzCouy75YQcwD%2FNvOH7aul5fuDo2GwRQRDXW1GXHpnqh0D%2BePFkEz3WWfW%2Bhaz3ZNWPgtQTuG93bhznpfILPOBbYTh12AGSim6%2BBdDMKdA%2FMDs0BgfYDxG0QG%2FU4MlyBykJNrlCQTaybSrStWsKI22E7mOT%2BKirh%2FZOTaq7Dvc4B4UHdsj6%2BuJ%2FjB%2BCyrIumNyHF1nnE9HHwX5CnH7xOxtk%2B9OSUobGWG%2FAo90HGhhaySxniFfmeGkWdqyJQd8u5kPqwgz%2FV%2FNaJMU0c3s%2F49W%2BoMB6Ey9Tm0Ucv1APvbYPe%2BWHhZgeQhWq8RMn32LyibbnxevIwq7TB7oEfbfpMcsp6TqW9gwS1VyY%2BcTudD4xGKx8bXT58c%2FzFAjozjzxNUCitNjwVkCbNVyQQ5Ya68uwm4rn19aopRDpSUYrUOn8AlkSaXyyFSrrpfV5sjypS5lzI1IgkiYqX9XjgYkovHRH58J5MEwomy3moN%2BtloZ5U9QIjsmGjN7adcmripIQGKXYXyi94MkQ89PvaLHxnRV3PzR3dwPMIHEgNMGOqUBdDX%2FCQHP1KAWDd7i2wkKo57flyuav0dGuv4l6KHZGhhVyEJ%2BFDx0o9JEgzZjIyL0YV6Ms1JobIugZvni1Znrr05XGQLa3S963Ra8zmRZs9CslxMiIhAv5x%2F3guM7SzMTfu7cdXd88UX3yQvsBQFRHqrJBuxad62xTsUsbA1Ot8XRnz7tlTqIFrtVYjmO7px3Xaw%2FnrlC2OIxMJImF9nVgU7YRjPW&X-Amz-Signature=bc6f86ee314f6aded0ff7f98aa0d4d5f04eac9b3d8ad2332ba5c85a73e829469&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46656RMAUFI%2F20260722%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260722T020641Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAIaCXVzLXdlc3QtMiJHMEUCIQCYsN8KdBvQvzSiaKhxU7BB8Y3f55OSu9RmKjLUzfnMOQIgY1%2FsLhPLeznM8jeku0915zdPG0Goo6FJNjYL9tm%2FRegqiAQIy%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDJJHBJwulP39oV12EyrcA%2BOClf5UzZ6HJGfDEVlDj3jp%2BL%2BWnkngwUt5E0QdQH4gn6QadSb12C%2FZPFmd0Lv3OFM%2FXoFIIWXWq1aK62FhPo7GPe%2FXoEUzCouy75YQcwD%2FNvOH7aul5fuDo2GwRQRDXW1GXHpnqh0D%2BePFkEz3WWfW%2Bhaz3ZNWPgtQTuG93bhznpfILPOBbYTh12AGSim6%2BBdDMKdA%2FMDs0BgfYDxG0QG%2FU4MlyBykJNrlCQTaybSrStWsKI22E7mOT%2BKirh%2FZOTaq7Dvc4B4UHdsj6%2BuJ%2FjB%2BCyrIumNyHF1nnE9HHwX5CnH7xOxtk%2B9OSUobGWG%2FAo90HGhhaySxniFfmeGkWdqyJQd8u5kPqwgz%2FV%2FNaJMU0c3s%2F49W%2BoMB6Ey9Tm0Ucv1APvbYPe%2BWHhZgeQhWq8RMn32LyibbnxevIwq7TB7oEfbfpMcsp6TqW9gwS1VyY%2BcTudD4xGKx8bXT58c%2FzFAjozjzxNUCitNjwVkCbNVyQQ5Ya68uwm4rn19aopRDpSUYrUOn8AlkSaXyyFSrrpfV5sjypS5lzI1IgkiYqX9XjgYkovHRH58J5MEwomy3moN%2BtloZ5U9QIjsmGjN7adcmripIQGKXYXyi94MkQ89PvaLHxnRV3PzR3dwPMIHEgNMGOqUBdDX%2FCQHP1KAWDd7i2wkKo57flyuav0dGuv4l6KHZGhhVyEJ%2BFDx0o9JEgzZjIyL0YV6Ms1JobIugZvni1Znrr05XGQLa3S963Ra8zmRZs9CslxMiIhAv5x%2F3guM7SzMTfu7cdXd88UX3yQvsBQFRHqrJBuxad62xTsUsbA1Ot8XRnz7tlTqIFrtVYjmO7px3Xaw%2FnrlC2OIxMJImF9nVgU7YRjPW&X-Amz-Signature=037ae2de6ebb6b1241d6d25161d0e4eabc66049246ca24574a08599b9d2d89b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







