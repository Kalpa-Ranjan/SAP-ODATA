



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z4BGBA7%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T024620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIEnVKGxRZeNWfPHYecCOkZ1sHcft2fXy0PyK7EQHKuxhAiBg40zJZKsbOY190p8XZnWiR6O9Rv217%2F5G04nx%2FnV8qiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLfGDrcxLp1%2B7usCTKtwDQvhndOdGl5s0SvTxx0GGWw%2BmKb8V3prYFpcLClwQJNYwZGlJoUzLMJi3uyufO2qMccTa%2BqMQKVrpNOQO1u3P4w5D7auIAJeIeTvJDu0YwwM%2Bti%2FW79Gg8EPXMf8d8sm8hTE4HCEz3PBhtWhVpOfDXyjTPE7rrKu%2B%2FCOu3%2BVLHsCJps0JzLY8KIEHaJtWXfQUOVKEoBvpvR%2Fm8KCpll765LlAdMYEMe%2FC2J8XKz%2BjmeXaUOTaVyFlZGA4bisOTfvfRoCz4%2BTMSBVTfgKpPDyImiF597OgPBdCD2c7E18rwUtyn0M49d28lcqc9c1P2FHz58xSzRVyudIS5GT%2Bs4TWRT9LLSE41Ct6Qx%2BU%2Bj3a1%2BOrObEenFoKJOysWYjy0kMrtg4Mkh133bYIfk%2FD%2BKodMoBWLGLLBoTyRni%2BpI1X2LZz3bwq7V4oGQB0dT0%2FqkzjJG8sRZH1y63jbVZWO9X8%2BborFKndnaUwnnkz6yX48%2Byn%2Bcjrwql3HVm%2BmuYnHVMx9c256c%2FgUD1SryXzRNwBPqQhpBe3GNJn3pBGBLDq402zSf%2FGBVYM6Ke2P1LUI2yw5NLb8lZD69dk75YbPtjReBeoj%2FGNQbZDUrQ1xFCaQHmJ4q12%2BXutXIuVpJcw%2F5Wv0AY6pgEbSTnJpttkVvdnhgeVHnkZPglaz3QuTUSDir1kWoCnVzMrlLjZAX2%2F%2BKZTpcjlx7WiAV5AUlJzFBxKTa%2BbFJCrggZqRcUquTOYK%2FTrSH31bkEU2ZeXws3B5%2FvZfiWfyhLP%2FmYmMaW4nx7%2F7dwewLi1K6zsTq%2Fcka9YZQ3iyFBdza5OKdz52liKdlGgOCYAq1wwdE%2Fe5fCj%2BrKI0lPr%2B0dGyd7Q5Ty6&X-Amz-Signature=7f4d01eedbc46363877c334551b23f5b289142e67646460f1355ce3e87ee2625&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4666Z4BGBA7%2F20260519%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260519T024620Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAMaCXVzLXdlc3QtMiJGMEQCIEnVKGxRZeNWfPHYecCOkZ1sHcft2fXy0PyK7EQHKuxhAiBg40zJZKsbOY190p8XZnWiR6O9Rv217%2F5G04nx%2FnV8qiqIBAjM%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMLfGDrcxLp1%2B7usCTKtwDQvhndOdGl5s0SvTxx0GGWw%2BmKb8V3prYFpcLClwQJNYwZGlJoUzLMJi3uyufO2qMccTa%2BqMQKVrpNOQO1u3P4w5D7auIAJeIeTvJDu0YwwM%2Bti%2FW79Gg8EPXMf8d8sm8hTE4HCEz3PBhtWhVpOfDXyjTPE7rrKu%2B%2FCOu3%2BVLHsCJps0JzLY8KIEHaJtWXfQUOVKEoBvpvR%2Fm8KCpll765LlAdMYEMe%2FC2J8XKz%2BjmeXaUOTaVyFlZGA4bisOTfvfRoCz4%2BTMSBVTfgKpPDyImiF597OgPBdCD2c7E18rwUtyn0M49d28lcqc9c1P2FHz58xSzRVyudIS5GT%2Bs4TWRT9LLSE41Ct6Qx%2BU%2Bj3a1%2BOrObEenFoKJOysWYjy0kMrtg4Mkh133bYIfk%2FD%2BKodMoBWLGLLBoTyRni%2BpI1X2LZz3bwq7V4oGQB0dT0%2FqkzjJG8sRZH1y63jbVZWO9X8%2BborFKndnaUwnnkz6yX48%2Byn%2Bcjrwql3HVm%2BmuYnHVMx9c256c%2FgUD1SryXzRNwBPqQhpBe3GNJn3pBGBLDq402zSf%2FGBVYM6Ke2P1LUI2yw5NLb8lZD69dk75YbPtjReBeoj%2FGNQbZDUrQ1xFCaQHmJ4q12%2BXutXIuVpJcw%2F5Wv0AY6pgEbSTnJpttkVvdnhgeVHnkZPglaz3QuTUSDir1kWoCnVzMrlLjZAX2%2F%2BKZTpcjlx7WiAV5AUlJzFBxKTa%2BbFJCrggZqRcUquTOYK%2FTrSH31bkEU2ZeXws3B5%2FvZfiWfyhLP%2FmYmMaW4nx7%2F7dwewLi1K6zsTq%2Fcka9YZQ3iyFBdza5OKdz52liKdlGgOCYAq1wwdE%2Fe5fCj%2BrKI0lPr%2B0dGyd7Q5Ty6&X-Amz-Signature=accac5f1547e053c149b7740bc2fbee917b46ce52f10c8ab594c29d3d7fcdb2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







