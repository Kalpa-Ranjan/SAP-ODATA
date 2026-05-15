



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHAYS4DX%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T135426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDYo7MxdcrKJYCjZ7wVB5fqqSL%2BdBn8uZK74knEvGgKEAiA8Wim2prWXcKAbPIksxaH5T6UnnqMWnXZFCeLYY53k%2FCr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMqDYhwFoG5XEbZac0KtwDt65J76WBad8YTBVAwLQ8NVCG9wMg875RaRCL2x1aV6Zd%2BM1zRQ%2BOhk7Hq1d3jzgScEnTpvMopbTvBd1t%2FngdU%2B3knZEB0e1iQ6c40uWLsJMjszbm1rwP687VvOuBBCMrA0%2BJpbM11zdvQDV07ZyPKF86%2Baegso9tOP0sv37oX6%2BP5eLIrxqsS6sy6bxb13ONc9pwbuTg6oYaj1NjGBhmIGZJ110mjQWo7DbFQDn1PBcaVGylKGvycP1%2BBi1aJprXNur1Lg0nyfoMPCKMQbXySKdz9%2FqyWnm3bXhLeZaBS7MzY7fueOAhZB3qINlrvwnOlvxbTxsRvfC8xG6jwjmsoxEA0wJLadzj0lYaJb%2BgFWrmQVect8Gn7d9aFPnUEvR42KTpFApyHvJvnGp7TD8fkQGtC0NP1IiXgT5nZj%2Fl0tfUPYnngH2SLzb0gxxVJDteyrx2Hx8x%2F4yjyNLoT7AMSIAST3ng%2Fy7UrxsSEDfgaqZgHuIYnv0zVkYIpH0P4hbLqWjOG4ApdMENIhsjX7fwd6OVywn2G3ugU%2F%2BijpZ0F5c780lhy3LqWTRxwaR%2B1ZDrf8qemzxaQs%2BattqrktR%2FDDn8gio17C1OkRbYi7n4DrEgS%2FlYLKSWfh8J%2BW4wl6mc0AY6pgHyXpxrwWI%2FNAwSyLLzB56B0iE6VWS%2BMj6ze0Hh0HpyseGXofGhvd%2F%2BEgnjuPQTIvd18hZ6X9K9LKF6EqyrspDVRGhup5jbjM6m5W5eJxF7FceRVPAgqwFjHJVYSgD2864l%2B82Oq%2FJBUiarXuRg7kk0FpY5tXJbeDPiELLTWkMaC7Wj0HBpXd2x0v%2BtjXNt%2BHGcF9jsFVkogB7fo27gmr4qak0Nxg%2Fz&X-Amz-Signature=93d906aa1d6d1c11d0f232d78d29386ed3d4193c0772dcd3417bcaa33d58ba2c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466RHAYS4DX%2F20260515%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260515T135426Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEK3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIDYo7MxdcrKJYCjZ7wVB5fqqSL%2BdBn8uZK74knEvGgKEAiA8Wim2prWXcKAbPIksxaH5T6UnnqMWnXZFCeLYY53k%2FCr%2FAwh2EAAaDDYzNzQyMzE4MzgwNSIMqDYhwFoG5XEbZac0KtwDt65J76WBad8YTBVAwLQ8NVCG9wMg875RaRCL2x1aV6Zd%2BM1zRQ%2BOhk7Hq1d3jzgScEnTpvMopbTvBd1t%2FngdU%2B3knZEB0e1iQ6c40uWLsJMjszbm1rwP687VvOuBBCMrA0%2BJpbM11zdvQDV07ZyPKF86%2Baegso9tOP0sv37oX6%2BP5eLIrxqsS6sy6bxb13ONc9pwbuTg6oYaj1NjGBhmIGZJ110mjQWo7DbFQDn1PBcaVGylKGvycP1%2BBi1aJprXNur1Lg0nyfoMPCKMQbXySKdz9%2FqyWnm3bXhLeZaBS7MzY7fueOAhZB3qINlrvwnOlvxbTxsRvfC8xG6jwjmsoxEA0wJLadzj0lYaJb%2BgFWrmQVect8Gn7d9aFPnUEvR42KTpFApyHvJvnGp7TD8fkQGtC0NP1IiXgT5nZj%2Fl0tfUPYnngH2SLzb0gxxVJDteyrx2Hx8x%2F4yjyNLoT7AMSIAST3ng%2Fy7UrxsSEDfgaqZgHuIYnv0zVkYIpH0P4hbLqWjOG4ApdMENIhsjX7fwd6OVywn2G3ugU%2F%2BijpZ0F5c780lhy3LqWTRxwaR%2B1ZDrf8qemzxaQs%2BattqrktR%2FDDn8gio17C1OkRbYi7n4DrEgS%2FlYLKSWfh8J%2BW4wl6mc0AY6pgHyXpxrwWI%2FNAwSyLLzB56B0iE6VWS%2BMj6ze0Hh0HpyseGXofGhvd%2F%2BEgnjuPQTIvd18hZ6X9K9LKF6EqyrspDVRGhup5jbjM6m5W5eJxF7FceRVPAgqwFjHJVYSgD2864l%2B82Oq%2FJBUiarXuRg7kk0FpY5tXJbeDPiELLTWkMaC7Wj0HBpXd2x0v%2BtjXNt%2BHGcF9jsFVkogB7fo27gmr4qak0Nxg%2Fz&X-Amz-Signature=ca0b3c6e9237721eb8f4055e9300b661774b8850a1fd1eac7b0a0f8b7d61995d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







