



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUKBOEMF%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T014957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIHmeQQrtRp4VZY5sbcfgB2TlrRM0iCN10AvAm8UoFeesAiEAnHAhWsQUikzSkVEQNLh3mqxxHB1b6%2B0AsWgq7cQcalwqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD8n3GjehBQ6QOEFSircA03E9GI1M0AiUUUC%2FcfzQTWKQzmRZxLXiFYXCI26TckpIMZmFCwdJJmGsBFDiEuYkF3FSAg%2FKdJgwqvvGP1g5ZR7Z5Yxk5xvm5SY8QWiKJPxGSL6rPcEd7dZqWGFeDj7IXazOwVv5nsl8oFwCLi94JxmD6aGf2mcJrugKwOJ9QqJ3jRAC2kKZNMpxNnY49ijhIZroZTcyqkkpmK7B9Hp%2FQPVopPIlNyk5F3XfDDGQXQwZpYWmNWqgsXgvoY7idqc4JY%2BJ%2FFWRTDph7%2FFpUccGj2HyiWhVpfR92GGQcbGJsh1gm1mJW6PO6P4akFAJupa8Jfkjg4cOMXO9tydoq5%2BtqkVC%2BkUmqm75B7OSc5yS0A4FH93Cz%2FMKiM%2BvxzFfA%2BbGppiuAUvoz0%2FZZY99opM4UVHbEzkCG9VHSLgSTyt6vSM5z0%2FetTulxJ2nabHZ4m9%2FNcmi0tAGPKeWshQ%2BrpjWPfXv6hDL%2FAaZNgktcP3xCf5CR47hJCtJ7zob%2FYZB%2F14CMhlTjMhaZXh559Ope09MNpwmPHkmATWCitc0rqjoDv9BpycmHk1xIxZY61GY7eyILKeldfyeSF1cw3T7r9XSFUsuHi47nL2IJvnCET0RmwmrqJhZuw0v0BzTC28MOfStMwGOqUBjI4x8TS7sxVmadUWY7MIpy0%2BCorVVJzscPm6t6uDFkiIQTkWMp%2FhBFrkZoKsZkolD2V8ESqs2tocDThS1MDN5yrWzpz3xkyO5A26N2vQvCJs9X%2BVJEiazGmVTCZnhkOOA9vNxLigSCp8sYjCDbP15K5uUz5PemnBPXdCWvBNXmOC9cbtcbqTVcqGkF63SGAIZTcxKF4ZRw4SwYnzZ5Ps8Nw1W3H%2B&X-Amz-Signature=3f058ef17277b6f6dc7350dec224f90323fa488d979e57ec9fff027a9eeb7b65&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YUKBOEMF%2F20260212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260212T014958Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAEaCXVzLXdlc3QtMiJHMEUCIHmeQQrtRp4VZY5sbcfgB2TlrRM0iCN10AvAm8UoFeesAiEAnHAhWsQUikzSkVEQNLh3mqxxHB1b6%2B0AsWgq7cQcalwqiAQIyv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDD8n3GjehBQ6QOEFSircA03E9GI1M0AiUUUC%2FcfzQTWKQzmRZxLXiFYXCI26TckpIMZmFCwdJJmGsBFDiEuYkF3FSAg%2FKdJgwqvvGP1g5ZR7Z5Yxk5xvm5SY8QWiKJPxGSL6rPcEd7dZqWGFeDj7IXazOwVv5nsl8oFwCLi94JxmD6aGf2mcJrugKwOJ9QqJ3jRAC2kKZNMpxNnY49ijhIZroZTcyqkkpmK7B9Hp%2FQPVopPIlNyk5F3XfDDGQXQwZpYWmNWqgsXgvoY7idqc4JY%2BJ%2FFWRTDph7%2FFpUccGj2HyiWhVpfR92GGQcbGJsh1gm1mJW6PO6P4akFAJupa8Jfkjg4cOMXO9tydoq5%2BtqkVC%2BkUmqm75B7OSc5yS0A4FH93Cz%2FMKiM%2BvxzFfA%2BbGppiuAUvoz0%2FZZY99opM4UVHbEzkCG9VHSLgSTyt6vSM5z0%2FetTulxJ2nabHZ4m9%2FNcmi0tAGPKeWshQ%2BrpjWPfXv6hDL%2FAaZNgktcP3xCf5CR47hJCtJ7zob%2FYZB%2F14CMhlTjMhaZXh559Ope09MNpwmPHkmATWCitc0rqjoDv9BpycmHk1xIxZY61GY7eyILKeldfyeSF1cw3T7r9XSFUsuHi47nL2IJvnCET0RmwmrqJhZuw0v0BzTC28MOfStMwGOqUBjI4x8TS7sxVmadUWY7MIpy0%2BCorVVJzscPm6t6uDFkiIQTkWMp%2FhBFrkZoKsZkolD2V8ESqs2tocDThS1MDN5yrWzpz3xkyO5A26N2vQvCJs9X%2BVJEiazGmVTCZnhkOOA9vNxLigSCp8sYjCDbP15K5uUz5PemnBPXdCWvBNXmOC9cbtcbqTVcqGkF63SGAIZTcxKF4ZRw4SwYnzZ5Ps8Nw1W3H%2B&X-Amz-Signature=da8a6e16911f2617b483c295566e2a19b34382dcb7793705c673beb7d85f3517&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







