



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNJQBHRE%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T140957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5lyhzF%2BfcoUdpiAJGmTL9R0WOYRgHiar%2B3svIM1EPAQIhALOWGAYW0guUIiF6L7cqZPHRzAGxmm9xl0bC36%2BxLjGXKogECLb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpYhZNk%2FHvLRZ21hoq3AOo%2By6OY%2BrpqXEkrlWLiPdYKUhksZujjhhvRP9bSJGpsW6PMfEGo6tZjfOwIvOJVsZIE16ITjY%2FYMTK5G7L59KZKAgYSc%2FdH1iGarQUtfQWF2zbSAdoyU6l8x4HP%2FrkYU8xV2kgozDda574%2ByDK4VHtzdeRiWHspUvqU6n3Rz182ewq86llgonQQCzrT%2BVox60wsD114qp76UoJdT9yMsBZyGmLiXPa%2FT%2FQtgFLAPGl0vUJfmdxeaavI6GrJ4gy%2FvkImdt7FocnNacU0dgEACN%2BQOarzXuHuco1%2B8mB5%2BggItCPsm9muw9eZWlS5Udp5bGEazTbBnSM0moPVx9etN00Z0medE%2B2rl76IW9RXrxjyjnne7%2FzBkjPoMYyWBe3G8PMkiOu8oIIL%2BRxHcUOXr7q7xiQ3ZFxLjZ53SqpyXLb79PjS1%2BSgRdc%2FNjQ2AYcclAFbC5xQbe0FIee5g2hPH4eLroWPKPwDya%2FSQ%2BQ0LNM3I47wEIfuY6Ice7CSm8NQ%2FwPI5bk1OiSBwPwnFnhiEFhlIDJzLtxk%2B2H6lZGoTpc9xnqT3NLMUTk1bWyL1gwRoIG%2BYcfXOAVnezu3apIboVGMDfAgvdxZ%2B7vXd3TmUOe8raneft%2FRlveLzmksjC81sPSBjqkAVUSdwYEPEmT8lTv5I56m%2Fr8xRlfb5Hbav7CzRhGnn2%2FQJejKYnDoUG5wx8oMrmTFJJSW2lYXyOEUuTsJ7QCE1HlbeIahaj%2FgbJoYOihbp62t%2BSVybNe746bjpRrZLfQOAfVoHGiiwItJ3SJu8AR%2Bf0wXqLGKMYQqsdRKYb7psfOmK4lMRS%2Bzt3hdEW%2BAJq79GEVQR%2B7c3f4D111aj2Pw1E2LsDu&X-Amz-Signature=243ec8711e47264c1ec4dbee085a2c25d3fd83a74500bfeba7927dbab5f27e42&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466SNJQBHRE%2F20260710%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260710T140957Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQD5lyhzF%2BfcoUdpiAJGmTL9R0WOYRgHiar%2B3svIM1EPAQIhALOWGAYW0guUIiF6L7cqZPHRzAGxmm9xl0bC36%2BxLjGXKogECLb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNjM3NDIzMTgzODA1IgxpYhZNk%2FHvLRZ21hoq3AOo%2By6OY%2BrpqXEkrlWLiPdYKUhksZujjhhvRP9bSJGpsW6PMfEGo6tZjfOwIvOJVsZIE16ITjY%2FYMTK5G7L59KZKAgYSc%2FdH1iGarQUtfQWF2zbSAdoyU6l8x4HP%2FrkYU8xV2kgozDda574%2ByDK4VHtzdeRiWHspUvqU6n3Rz182ewq86llgonQQCzrT%2BVox60wsD114qp76UoJdT9yMsBZyGmLiXPa%2FT%2FQtgFLAPGl0vUJfmdxeaavI6GrJ4gy%2FvkImdt7FocnNacU0dgEACN%2BQOarzXuHuco1%2B8mB5%2BggItCPsm9muw9eZWlS5Udp5bGEazTbBnSM0moPVx9etN00Z0medE%2B2rl76IW9RXrxjyjnne7%2FzBkjPoMYyWBe3G8PMkiOu8oIIL%2BRxHcUOXr7q7xiQ3ZFxLjZ53SqpyXLb79PjS1%2BSgRdc%2FNjQ2AYcclAFbC5xQbe0FIee5g2hPH4eLroWPKPwDya%2FSQ%2BQ0LNM3I47wEIfuY6Ice7CSm8NQ%2FwPI5bk1OiSBwPwnFnhiEFhlIDJzLtxk%2B2H6lZGoTpc9xnqT3NLMUTk1bWyL1gwRoIG%2BYcfXOAVnezu3apIboVGMDfAgvdxZ%2B7vXd3TmUOe8raneft%2FRlveLzmksjC81sPSBjqkAVUSdwYEPEmT8lTv5I56m%2Fr8xRlfb5Hbav7CzRhGnn2%2FQJejKYnDoUG5wx8oMrmTFJJSW2lYXyOEUuTsJ7QCE1HlbeIahaj%2FgbJoYOihbp62t%2BSVybNe746bjpRrZLfQOAfVoHGiiwItJ3SJu8AR%2Bf0wXqLGKMYQqsdRKYb7psfOmK4lMRS%2Bzt3hdEW%2BAJq79GEVQR%2B7c3f4D111aj2Pw1E2LsDu&X-Amz-Signature=e7f7b09e82739504480b6cb9032b1634d419468e277cfb68515df2b1ef024187&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







