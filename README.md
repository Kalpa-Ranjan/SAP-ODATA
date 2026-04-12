



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIBY62UX%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T070734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE5PBOc8Gpygc0%2FkPoebEVtA%2BhZZ2mxBSfWkBIP8HjSaAiEA4fgWxfji7NKK%2FJLHB7SJe7P70YhODpjQXOcTZTVSIrEq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDPwtTRoYIMAI4mxz1CrcA4tKVKEcqpRMK%2BeCv6FDIVZOblUKXNjsyMI%2Fg9RlOvPO8vhi77JRt4Ivmg2St3aX7NgKHWRqMyOfAxep7xRTYfTd2sOtFRSdCBw8npXBBEhKFU69%2F2qSnjYEdsP7QHiNFIAsUebOqpprpfmNVBkJfgekTC8O0bBCUgB%2BFMkDMq%2BuiG4JNymb%2BjlXyl8Qp4JW9C%2FK78EMnb6DzZ%2Fypd5AKj4VDGZ9%2BKJE5jarVlYtQ%2Fy07Vs%2Bdread0jk%2BGh6WCmRlczmhRs7a3t2l%2B9DgCt9v5QPwsmgbuOM%2ByE9EirIVXclqgaBn5fNtema%2FGVwqQ9KJ8Ozx3xwPzMN3655wQ2PktfSOXAj%2FWLYNt5ztdBjPEmEU6Osl8gbrDUey4fBQ%2FktyJwJz3JUOSWRE706vKo%2Bk8Bh0TRLmOMaBc1XGjSdlolbxvwRY%2FuTDL%2Bg32siqImEVU%2BywH9V6KTWyxFgKYOehA6f%2FbVltUEoUolcgsw%2BRvZS2BkbI9XkkchR5wivFlWY5AuuG0YF%2FsggRtMoaXmtQo%2BW7UMR0vlUHab22nDFw%2B6oCoRMfzcp7FtpbvCEKCJB68QI6oF3mspeH8IsIwjolyafathlaX7gYg6ma7bsRgHiY7TTzYiaZ881iEgaMN307M4GOqUB4m7VAGbKQVRyW9mFuTv1GZ7my0bBBwUEBIxgClt9QTNTpkxO6hDEy4LLiGRec8FpC699l03UEHE9B1CEBXEzQWs%2F0zoIuGiku9dhN0%2BKrilvQPHvjJblis%2FGeVKHYcXKr6vxWBnj0XZxHlxTB3MRPUe98hYUFIJRlLW5xIWK6FjI4rnK3VoarKivC8xvRbfe7xLdIYO0Y0rQSk0KbL1iYSBwJpOj&X-Amz-Signature=4c0e3b9d77c75cd1bcf00ec2b430ca4c2ee3143a1fb3c0a52d14c81f772aaf08&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XIBY62UX%2F20260412%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260412T070734Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEI%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIE5PBOc8Gpygc0%2FkPoebEVtA%2BhZZ2mxBSfWkBIP8HjSaAiEA4fgWxfji7NKK%2FJLHB7SJe7P70YhODpjQXOcTZTVSIrEq%2FwMIVxAAGgw2Mzc0MjMxODM4MDUiDPwtTRoYIMAI4mxz1CrcA4tKVKEcqpRMK%2BeCv6FDIVZOblUKXNjsyMI%2Fg9RlOvPO8vhi77JRt4Ivmg2St3aX7NgKHWRqMyOfAxep7xRTYfTd2sOtFRSdCBw8npXBBEhKFU69%2F2qSnjYEdsP7QHiNFIAsUebOqpprpfmNVBkJfgekTC8O0bBCUgB%2BFMkDMq%2BuiG4JNymb%2BjlXyl8Qp4JW9C%2FK78EMnb6DzZ%2Fypd5AKj4VDGZ9%2BKJE5jarVlYtQ%2Fy07Vs%2Bdread0jk%2BGh6WCmRlczmhRs7a3t2l%2B9DgCt9v5QPwsmgbuOM%2ByE9EirIVXclqgaBn5fNtema%2FGVwqQ9KJ8Ozx3xwPzMN3655wQ2PktfSOXAj%2FWLYNt5ztdBjPEmEU6Osl8gbrDUey4fBQ%2FktyJwJz3JUOSWRE706vKo%2Bk8Bh0TRLmOMaBc1XGjSdlolbxvwRY%2FuTDL%2Bg32siqImEVU%2BywH9V6KTWyxFgKYOehA6f%2FbVltUEoUolcgsw%2BRvZS2BkbI9XkkchR5wivFlWY5AuuG0YF%2FsggRtMoaXmtQo%2BW7UMR0vlUHab22nDFw%2B6oCoRMfzcp7FtpbvCEKCJB68QI6oF3mspeH8IsIwjolyafathlaX7gYg6ma7bsRgHiY7TTzYiaZ881iEgaMN307M4GOqUB4m7VAGbKQVRyW9mFuTv1GZ7my0bBBwUEBIxgClt9QTNTpkxO6hDEy4LLiGRec8FpC699l03UEHE9B1CEBXEzQWs%2F0zoIuGiku9dhN0%2BKrilvQPHvjJblis%2FGeVKHYcXKr6vxWBnj0XZxHlxTB3MRPUe98hYUFIJRlLW5xIWK6FjI4rnK3VoarKivC8xvRbfe7xLdIYO0Y0rQSk0KbL1iYSBwJpOj&X-Amz-Signature=939d43c4104612ff5b97321cf13c9de570cb97d8bdd8c74232f826e129bbb45c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







