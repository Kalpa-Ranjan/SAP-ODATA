



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZQLK3WU%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T015139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQCMLDuLsEdLXWJNHQlYpoUCq%2FmzNFbp0Pa46ipQXRO%2BvAIgMNI1ixxpdoGaOfUELpwXVUT6OWn2txB1yCs1mktYbzwq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGUKZpM8LGpvScfpNircA%2B4j9jSwA306Qz5fTBvYwziLJowPuluPLAGA1Qwuw1MLMLo3rTGI5dhUD4hZf5nDaJ2MjKWOg7dXrYlpQ%2FkzlKg9zQN07OqruAIp73yLCJPxfeHwPJQOOREkXQ53JYqzuIoDXhaR3L6EcC6nAOkxJSxJANK6kW%2Bzq2FIFQiIDQJt4PJzz7Uvg29SMKXpY8oxUEtoaZxIok3NN7SruZbNV%2BQ6Hb5HllLUvCzx2%2FrGrdMhBoqaXCLUKfJAyzqR6ISHJC3NTRYbkcaDxlKRoLwjsr%2FxMEIqEy0Do08vkhvRsUdnj%2BJRJufPghhmwmh6Ra9bmjF6w6N8MSUd68cH%2Fka7OKGu52Wze6ZGJcwPATPcXFHTJNhwuZmQcCzDkE7vwksYQywla5FgPlJkNZOK%2B9P7HrsTCdJmZGLeafQ%2FbxmhhWnrIA64DpGrMY6fsPgpjudkt1MVv4TfitRjj4PMoByHSK9MY4W%2FQ7OZz0NLQBFX%2BJtd1FepkzHpby6OL19WTWe5WordgTXnHFrchQaHnTvgUcFSEnMOKKjpQJCIDs3y4J%2Begk7b3OU9vNvFvMtvuJj177Wl%2BUl%2B277sj7gD4TYB0KTlkAQKIlWici1b8ldtfzjBpma74JPKDO22HhYNMI%2BfxMwGOqUBNpy1y2ryOEz6UbxNDNvJIJ3QcK1iI9s8%2F%2Fi%2FvAm3MVWv1Oep7v0HJo31qhrYHd22f1sB%2FNZSZRdWMZ9XTMgIDNNsUESdj7F7r%2FbTg4jvG45VVn6pCFroVcalwjOLAoQGulw%2FW8%2Fle%2FYCqYxHNU%2FctfFMDVkCBhKHe9qaEWVHb7kdNnNAN21Jhvs23tARfQfKPXU1pOdYgY%2BVyw%2FD9Q98lM989sMT&X-Amz-Signature=5c91aa78636467db5d8f739d7f0e17aff0c4f6068ea1b6758b1147d5a9ab5d32&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WZQLK3WU%2F20260215%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260215T015139Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIQCMLDuLsEdLXWJNHQlYpoUCq%2FmzNFbp0Pa46ipQXRO%2BvAIgMNI1ixxpdoGaOfUELpwXVUT6OWn2txB1yCs1mktYbzwq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDGUKZpM8LGpvScfpNircA%2B4j9jSwA306Qz5fTBvYwziLJowPuluPLAGA1Qwuw1MLMLo3rTGI5dhUD4hZf5nDaJ2MjKWOg7dXrYlpQ%2FkzlKg9zQN07OqruAIp73yLCJPxfeHwPJQOOREkXQ53JYqzuIoDXhaR3L6EcC6nAOkxJSxJANK6kW%2Bzq2FIFQiIDQJt4PJzz7Uvg29SMKXpY8oxUEtoaZxIok3NN7SruZbNV%2BQ6Hb5HllLUvCzx2%2FrGrdMhBoqaXCLUKfJAyzqR6ISHJC3NTRYbkcaDxlKRoLwjsr%2FxMEIqEy0Do08vkhvRsUdnj%2BJRJufPghhmwmh6Ra9bmjF6w6N8MSUd68cH%2Fka7OKGu52Wze6ZGJcwPATPcXFHTJNhwuZmQcCzDkE7vwksYQywla5FgPlJkNZOK%2B9P7HrsTCdJmZGLeafQ%2FbxmhhWnrIA64DpGrMY6fsPgpjudkt1MVv4TfitRjj4PMoByHSK9MY4W%2FQ7OZz0NLQBFX%2BJtd1FepkzHpby6OL19WTWe5WordgTXnHFrchQaHnTvgUcFSEnMOKKjpQJCIDs3y4J%2Begk7b3OU9vNvFvMtvuJj177Wl%2BUl%2B277sj7gD4TYB0KTlkAQKIlWici1b8ldtfzjBpma74JPKDO22HhYNMI%2BfxMwGOqUBNpy1y2ryOEz6UbxNDNvJIJ3QcK1iI9s8%2F%2Fi%2FvAm3MVWv1Oep7v0HJo31qhrYHd22f1sB%2FNZSZRdWMZ9XTMgIDNNsUESdj7F7r%2FbTg4jvG45VVn6pCFroVcalwjOLAoQGulw%2FW8%2Fle%2FYCqYxHNU%2FctfFMDVkCBhKHe9qaEWVHb7kdNnNAN21Jhvs23tARfQfKPXU1pOdYgY%2BVyw%2FD9Q98lM989sMT&X-Amz-Signature=5e8b3e880622247df861f4a0396a1fa667a93cca6ecaf001b8b6da345a77e64f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







