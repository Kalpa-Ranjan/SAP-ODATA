



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642MHY7UW%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T011248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpNCmj6aKHlEUUqIHHNVsc45H0MLNueKrXYg5vzjJB9AIgBuyF4m2LSEUXaL5QUdrm85hvMuGwfuYR0%2F8rdKPTCRoq%2FwMIchAAGgw2Mzc0MjMxODM4MDUiDHapiePw0AjdvCduVircA6NAkQgB8yZzTmc%2FbELGsBD%2Fdj8%2FsrKpie3VWt6f%2BGKFI70ilLgdZmp3lKhxtz0DXBdkdZHzrmyi9NiZH2WPaLHqDm4mpWbUUFdwkXtBJauzXemdcJRy9J6eSFgPVMDLiFbSFnu%2FZM4sJR810JFJl5jfrS3kmqCVSDWqFuYroAPBDBJ6Y0IY0mQlY%2FWTAjh4Tir02QWaY7Jw7eaLqk%2FIuzR99MdPbzHygsk8xAcW8Nvahd0RaRnq8TVrgUtMeFWqWbWC9FUnhnPjfKdOmN1LdDgaf0iehWSQuutMce9R0VvHsfFhdpJ%2BUxoYLC1h0bpHA3VNSgwFCcxGaJjCSETyQ3ZKn7pfkLRW0BbPEpFMxzhzYrW9h4VoO%2BQlwaJavaaUX7ix3%2FrjPPDlDwWJ7VqT3RMBNHTP8Vb3EZ66lXEVaLOgtlD5SZFgzaLdyEUSHJ96OEwqmMVb9z%2F0eM%2FkfPh6i0f%2Bqxm0uYSQo8ghS05jvAu%2BL7LWQ6thAqoRkIac%2FClK7F10Fv4pXfmv98%2BSSdcLVAKc6etHxmr3CJsEugL7zDQXFIYnonxR3di6F9tREEKO1e%2F72gNEPDAxwS2jbmhk%2B58vq5fSBO1nn1%2FMyPeJyXqrrDkmEG6BGkUbocliMLb6h8oGOqUBHFZ%2F5XsCDXTeIkESBEWCzoUaSMJNiVfTCHckB0qLwmXc1cUfzQQ2Hk2FLCAOmG4iAk5bqTI71IGXnJDyXV%2BLou8cgA%2BwvZL4VAwI0B5nz4bm8t3Sv19lIG%2BsBIWX716Cq1bR1uMN6nzxTepyuG%2BYg91w1HJ3rLvnOry9RV7SwQUeWvwjltoCA82ENuommJkbAfxT1AYJIJNwcFR3vdq8WkdvXArc&X-Amz-Signature=44cbf6772584a27dab850bf0cddecdf76e2eedc886b8b5e1b0225b5e2bf95057&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46642MHY7UW%2F20251217%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251217T011248Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQCpNCmj6aKHlEUUqIHHNVsc45H0MLNueKrXYg5vzjJB9AIgBuyF4m2LSEUXaL5QUdrm85hvMuGwfuYR0%2F8rdKPTCRoq%2FwMIchAAGgw2Mzc0MjMxODM4MDUiDHapiePw0AjdvCduVircA6NAkQgB8yZzTmc%2FbELGsBD%2Fdj8%2FsrKpie3VWt6f%2BGKFI70ilLgdZmp3lKhxtz0DXBdkdZHzrmyi9NiZH2WPaLHqDm4mpWbUUFdwkXtBJauzXemdcJRy9J6eSFgPVMDLiFbSFnu%2FZM4sJR810JFJl5jfrS3kmqCVSDWqFuYroAPBDBJ6Y0IY0mQlY%2FWTAjh4Tir02QWaY7Jw7eaLqk%2FIuzR99MdPbzHygsk8xAcW8Nvahd0RaRnq8TVrgUtMeFWqWbWC9FUnhnPjfKdOmN1LdDgaf0iehWSQuutMce9R0VvHsfFhdpJ%2BUxoYLC1h0bpHA3VNSgwFCcxGaJjCSETyQ3ZKn7pfkLRW0BbPEpFMxzhzYrW9h4VoO%2BQlwaJavaaUX7ix3%2FrjPPDlDwWJ7VqT3RMBNHTP8Vb3EZ66lXEVaLOgtlD5SZFgzaLdyEUSHJ96OEwqmMVb9z%2F0eM%2FkfPh6i0f%2Bqxm0uYSQo8ghS05jvAu%2BL7LWQ6thAqoRkIac%2FClK7F10Fv4pXfmv98%2BSSdcLVAKc6etHxmr3CJsEugL7zDQXFIYnonxR3di6F9tREEKO1e%2F72gNEPDAxwS2jbmhk%2B58vq5fSBO1nn1%2FMyPeJyXqrrDkmEG6BGkUbocliMLb6h8oGOqUBHFZ%2F5XsCDXTeIkESBEWCzoUaSMJNiVfTCHckB0qLwmXc1cUfzQQ2Hk2FLCAOmG4iAk5bqTI71IGXnJDyXV%2BLou8cgA%2BwvZL4VAwI0B5nz4bm8t3Sv19lIG%2BsBIWX716Cq1bR1uMN6nzxTepyuG%2BYg91w1HJ3rLvnOry9RV7SwQUeWvwjltoCA82ENuommJkbAfxT1AYJIJNwcFR3vdq8WkdvXArc&X-Amz-Signature=736fdf238fd2e5aec45b1a74cc6a4ac7cfcb016061b64f5e8fcaad9cb05ba9da&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







