



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BBDXBG%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T182138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGvZsTVf8CXOG4Kb0saSNKoQ%2FAXWK3jVfVt5KZ7%2FmUKMAiEAr2gtYxNsl%2Fb4%2FmwWEUpE%2FUP1u5n20GHr1W8IoXu5rq0qiAQIov%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkLIUyYPN9x%2BZMetircAycUkeOS%2FyKjosrDG9WVQ4DJ2ui%2BOhXa7rC0%2BsSD6cuhvZJWxR6QyZsHwqY7NyXepR1NPepm%2FyHpXgnudCUGv8keCUTIAlicDTC3cahq8PtKVxgUtOqIAHu%2BSNgwh4UBXv5xTiDYoRrvvUt%2BzrMlzUVTrtgySsbqpQjLdCw%2FNoW3UKGvwDrroh8PyllF%2BRHFoMIcySZlqQUMkVCDf%2BC78%2B5SPjeRXcUYEg%2FCZSg6%2FkfnYcjZ%2Bk5Jeqi4XBAHoO2UT8Wf3GH1eNp8yI%2F9sRrTDMLnxxw7y1LkT6UEzeaygCC3l4T1E9%2B548hnnzXq75I5vP8zjwY6K79OP7b6j2Wd%2BSPC5B4JWHYtudgJFBHjuBfY%2BZACLgK%2FGbPhcwmn17R3FHBYwb4pEiavYnjv5KCrO%2F1b4ak8uEfWVBeJtJhYEPb9wEg7HaQ39voQA7wfnXsI5Au0FIDDmbs83kTSh1bsmD0drlAzJE%2ByeGTtJqsFZ3TRP0wOAMU0zQyxattBsU%2BziCbLS9yXCnhN23w6cNtB9Zje3XZO6KF6DehSrm9Y3AWjop5NDrw4wje6ldPyIQBewilBEm9Xwq%2BaWGCRLjMj9qe4%2FvfgV%2BVQT0O70cvjp%2BPtqF%2FDFVS2EtIR%2F3hnMNb6ockGOqUB8chvwsFmEK2O8P8FmEEa%2BgB6HxWaAE0J1jW1bVuSd%2FCzfdTx%2FgUQllNUB2Ef806OKp5OeJ1jIFFnzQ0GGOLipebeiT8g9uvqFhgaVapZS0dLNVvzDxmlhy7rBXl9n6ywV%2BU5kUxYd1EiLjOmDYmyNeK%2Fc7Tk9LIdvDVrMz93EyPSX%2BfVT9OnJhjN3sbo1KCvknWDSfz1bUcJ6pkn45wte2%2FX3CGN&X-Amz-Signature=1cc318c1a91157286fda69b282968dd420a68b596930312fc98f123bac88e701&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466Q3BBDXBG%2F20251127%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251127T182138Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjENn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIGvZsTVf8CXOG4Kb0saSNKoQ%2FAXWK3jVfVt5KZ7%2FmUKMAiEAr2gtYxNsl%2Fb4%2FmwWEUpE%2FUP1u5n20GHr1W8IoXu5rq0qiAQIov%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDLkLIUyYPN9x%2BZMetircAycUkeOS%2FyKjosrDG9WVQ4DJ2ui%2BOhXa7rC0%2BsSD6cuhvZJWxR6QyZsHwqY7NyXepR1NPepm%2FyHpXgnudCUGv8keCUTIAlicDTC3cahq8PtKVxgUtOqIAHu%2BSNgwh4UBXv5xTiDYoRrvvUt%2BzrMlzUVTrtgySsbqpQjLdCw%2FNoW3UKGvwDrroh8PyllF%2BRHFoMIcySZlqQUMkVCDf%2BC78%2B5SPjeRXcUYEg%2FCZSg6%2FkfnYcjZ%2Bk5Jeqi4XBAHoO2UT8Wf3GH1eNp8yI%2F9sRrTDMLnxxw7y1LkT6UEzeaygCC3l4T1E9%2B548hnnzXq75I5vP8zjwY6K79OP7b6j2Wd%2BSPC5B4JWHYtudgJFBHjuBfY%2BZACLgK%2FGbPhcwmn17R3FHBYwb4pEiavYnjv5KCrO%2F1b4ak8uEfWVBeJtJhYEPb9wEg7HaQ39voQA7wfnXsI5Au0FIDDmbs83kTSh1bsmD0drlAzJE%2ByeGTtJqsFZ3TRP0wOAMU0zQyxattBsU%2BziCbLS9yXCnhN23w6cNtB9Zje3XZO6KF6DehSrm9Y3AWjop5NDrw4wje6ldPyIQBewilBEm9Xwq%2BaWGCRLjMj9qe4%2FvfgV%2BVQT0O70cvjp%2BPtqF%2FDFVS2EtIR%2F3hnMNb6ockGOqUB8chvwsFmEK2O8P8FmEEa%2BgB6HxWaAE0J1jW1bVuSd%2FCzfdTx%2FgUQllNUB2Ef806OKp5OeJ1jIFFnzQ0GGOLipebeiT8g9uvqFhgaVapZS0dLNVvzDxmlhy7rBXl9n6ywV%2BU5kUxYd1EiLjOmDYmyNeK%2Fc7Tk9LIdvDVrMz93EyPSX%2BfVT9OnJhjN3sbo1KCvknWDSfz1bUcJ6pkn45wte2%2FX3CGN&X-Amz-Signature=46102a7c9348aecc23a09701435b5c6197ddd8c2f0f323c4afd2ef583647fc2e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







