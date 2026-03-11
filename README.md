



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6EX47UC%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T184733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2Xr%2FNoZKp7tA%2FKqwsqulz2VARN6e2%2FfESG9gSkGk9BQIgWmCNVCTgq1NiYi6v%2Fy96yWpoAhaXBGpRS7yQzz8YGvYq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDMegkGtbQN5V7IKyeyrcA%2Fa8Y8IJ9gDlZHEsHRT8Thgd2AjxZyEcRXH4XNqZ3rsiG8fESzh6GrEY8xv8vEhc8uQXQWhmqlIkAsMkFAQlQ%2FMZmLhTVRojkQGGwGta2dU%2FoMoBlG9m9RPMy0tJ5LV9c1mKO3vofjCx5oLlMUZmPtqdpgev2xlwL2b2MT5%2BjTKGywIWO19DZfG9GsvLDw5RKYEhkbPfsqWqNnUkMi11PIoBKjRcDNZed9%2FepIZqserlmI8kJDZr4cIDCpstn150obd7SQwvU1YdQIlgySuK42yFZRqpibbHc%2F%2Bildt04DgUQDavw2vHV%2BirvBY2aLCpxj22N0DhXzWMYFQWZ8nB%2BCKpnhBmEgyR5VC0iFZwJR4Q7lchJ6%2B%2BTI4mH%2FQNXFksrDcqZBA0mTW26wn17IPHcFK6pNhgj%2BvZgchH3CfLiYsj8aHnf%2FwTQhUv5a85VAdMTV6ngkihciT1pdHrLgF7mauIWqpTNJ46n55GCwPuRi7ioHHoRT7jhPLqhlzYocWM7zjsY5nrNz0kM8KRqtKUl61wqylaTA7FAWPhXRa4rhYBGqXEQV%2BXiYqAdui4SobTuwWFqk2O140ZNQ33FSZxubULi8WL%2Fd63PG2mbJrT4qJS2MPlTAdXPO1wa6kmMOOWxs0GOqUBUy2c7Oa18QjCFpe603LtzK%2FsZSfAxGzRNGQr%2BvSKWOSHKRPLJYfjWpNKFcRVjF39scz%2FQc6%2FwhPCR1q4RjannDllzC5hFfnd9YGe2Y25KcfJtGDONkuiPi8NKh2Qi1g2xOUBpYghPikaTKT1K4VNsiPA2IaH%2BALZX9rrcaLzakS8byIAkWGsVfupHcC9hyqYU2IOxcdXweq89bbnT41isS1lkBhE&X-Amz-Signature=6266aac154b69d3e181a8aa06c2308ec52c801340a9c4ac773c84f1bd7edf1e6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X6EX47UC%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T184733Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJj%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIQC2Xr%2FNoZKp7tA%2FKqwsqulz2VARN6e2%2FfESG9gSkGk9BQIgWmCNVCTgq1NiYi6v%2Fy96yWpoAhaXBGpRS7yQzz8YGvYq%2FwMIYRAAGgw2Mzc0MjMxODM4MDUiDMegkGtbQN5V7IKyeyrcA%2Fa8Y8IJ9gDlZHEsHRT8Thgd2AjxZyEcRXH4XNqZ3rsiG8fESzh6GrEY8xv8vEhc8uQXQWhmqlIkAsMkFAQlQ%2FMZmLhTVRojkQGGwGta2dU%2FoMoBlG9m9RPMy0tJ5LV9c1mKO3vofjCx5oLlMUZmPtqdpgev2xlwL2b2MT5%2BjTKGywIWO19DZfG9GsvLDw5RKYEhkbPfsqWqNnUkMi11PIoBKjRcDNZed9%2FepIZqserlmI8kJDZr4cIDCpstn150obd7SQwvU1YdQIlgySuK42yFZRqpibbHc%2F%2Bildt04DgUQDavw2vHV%2BirvBY2aLCpxj22N0DhXzWMYFQWZ8nB%2BCKpnhBmEgyR5VC0iFZwJR4Q7lchJ6%2B%2BTI4mH%2FQNXFksrDcqZBA0mTW26wn17IPHcFK6pNhgj%2BvZgchH3CfLiYsj8aHnf%2FwTQhUv5a85VAdMTV6ngkihciT1pdHrLgF7mauIWqpTNJ46n55GCwPuRi7ioHHoRT7jhPLqhlzYocWM7zjsY5nrNz0kM8KRqtKUl61wqylaTA7FAWPhXRa4rhYBGqXEQV%2BXiYqAdui4SobTuwWFqk2O140ZNQ33FSZxubULi8WL%2Fd63PG2mbJrT4qJS2MPlTAdXPO1wa6kmMOOWxs0GOqUBUy2c7Oa18QjCFpe603LtzK%2FsZSfAxGzRNGQr%2BvSKWOSHKRPLJYfjWpNKFcRVjF39scz%2FQc6%2FwhPCR1q4RjannDllzC5hFfnd9YGe2Y25KcfJtGDONkuiPi8NKh2Qi1g2xOUBpYghPikaTKT1K4VNsiPA2IaH%2BALZX9rrcaLzakS8byIAkWGsVfupHcC9hyqYU2IOxcdXweq89bbnT41isS1lkBhE&X-Amz-Signature=5cfb0a4b6237b190f1e6052614c0dde589d34642494aec934b0e25156b149d01&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







