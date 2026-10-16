



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVLE3G7Z%2F20261016%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261016T180855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJGMEQCIFe%2B2OCmpx613sMSMEcdEoCpe8ZMJ1HZmhvLgPRJ6N6yAiB0zwjWE2PRsZPYeohu3tT8QpaqPxoSKQgbag54y4wpMyqIBAjp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMldrZZC%2BlytGmUU44KtwDAEEw9MY%2FogvRd5CsHyF3K5i5tElbMu%2Bj7lygKcBxPQf7GqBrir7Jhl2NW9E1zCKmAi1wHueaAALuG7EAQFixDzpoagaoPzLB3wEJp5rNHacfPDG5c0rmywTfaHrqDBNo6NSt8RxVaADQ3hPJuy9RJh%2BNkjZ1IHwKzYXshJJwT4oKl24P%2FKzN7f6ZXOLtc6ibfSTxDjWJWBnDTM8O6rOWZFdQJUkU6t6xMy1MakGnTvuipnTF%2BIBoNOiMEFw%2BTtEnIxA1pUjc%2BDnH%2FAueGClQjnQHDUJVAyiGSaI5Fvs0pn8%2BsaIDviALZJm6uQlLLJn8OmNllSk3BL6cLU%2BtWZFQOUIzy7Wz1MuXhnNvh9lYWrJDZdE8AFXG2PYbLbA4erYA%2BsGURKJngPJI2fbNH%2FlsTqlJV6lQ0A2U3p57T2uJefhPVms0BTgdSqtOSzOh3bhPhWB%2F0eRx%2BfAHyi2zRYHaD8TQt%2FLgPVVqomS34sqXYomAKkusLHxY6hiSB03KUBKrmSvSyH2%2FFtWAj0yaJAtDQ3uPR8EdPTlZRwgi26vA7oI9tm03qkVsNWrQP2xxtw0Tv7wuBkoXJVKjMeQ%2FGEZ20jmHP4W3UfyNPcj0hiaUhKahb1a8j3kI5rr9YUMwqK3J1gY6pgHmWfYlrnBAc8EIYxPKet%2Bgbu8X8sAXE8e2GNPnP70d5R1yB6jzU2HhKOKagvptLoREWmygqEAjgM0l3l64CJWEktIa0Gfl%2BslDppYO8jUtKuojCEQowHKxjvgLpeJSJfnwGa9C%2Faj6%2B2NESDqbW4TRqGuiEUf3Mtjuiawp%2B0e9xMNAION32co0j1FD%2FCv5zLnRT00ocZgfw%2F5TZA%2BIPQsp6iCel9GP&X-Amz-Signature=c6b485132b702cf8ba8d03c87c1cc9a737efed5754e3b3ec2f05fe954ed19c75&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XVLE3G7Z%2F20261016%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261016T180855Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjECEaCXVzLXdlc3QtMiJGMEQCIFe%2B2OCmpx613sMSMEcdEoCpe8ZMJ1HZmhvLgPRJ6N6yAiB0zwjWE2PRsZPYeohu3tT8QpaqPxoSKQgbag54y4wpMyqIBAjp%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMldrZZC%2BlytGmUU44KtwDAEEw9MY%2FogvRd5CsHyF3K5i5tElbMu%2Bj7lygKcBxPQf7GqBrir7Jhl2NW9E1zCKmAi1wHueaAALuG7EAQFixDzpoagaoPzLB3wEJp5rNHacfPDG5c0rmywTfaHrqDBNo6NSt8RxVaADQ3hPJuy9RJh%2BNkjZ1IHwKzYXshJJwT4oKl24P%2FKzN7f6ZXOLtc6ibfSTxDjWJWBnDTM8O6rOWZFdQJUkU6t6xMy1MakGnTvuipnTF%2BIBoNOiMEFw%2BTtEnIxA1pUjc%2BDnH%2FAueGClQjnQHDUJVAyiGSaI5Fvs0pn8%2BsaIDviALZJm6uQlLLJn8OmNllSk3BL6cLU%2BtWZFQOUIzy7Wz1MuXhnNvh9lYWrJDZdE8AFXG2PYbLbA4erYA%2BsGURKJngPJI2fbNH%2FlsTqlJV6lQ0A2U3p57T2uJefhPVms0BTgdSqtOSzOh3bhPhWB%2F0eRx%2BfAHyi2zRYHaD8TQt%2FLgPVVqomS34sqXYomAKkusLHxY6hiSB03KUBKrmSvSyH2%2FFtWAj0yaJAtDQ3uPR8EdPTlZRwgi26vA7oI9tm03qkVsNWrQP2xxtw0Tv7wuBkoXJVKjMeQ%2FGEZ20jmHP4W3UfyNPcj0hiaUhKahb1a8j3kI5rr9YUMwqK3J1gY6pgHmWfYlrnBAc8EIYxPKet%2Bgbu8X8sAXE8e2GNPnP70d5R1yB6jzU2HhKOKagvptLoREWmygqEAjgM0l3l64CJWEktIa0Gfl%2BslDppYO8jUtKuojCEQowHKxjvgLpeJSJfnwGa9C%2Faj6%2B2NESDqbW4TRqGuiEUf3Mtjuiawp%2B0e9xMNAION32co0j1FD%2FCv5zLnRT00ocZgfw%2F5TZA%2BIPQsp6iCel9GP&X-Amz-Signature=109ea98ca4d1ad7e3a69298a0005c7d4511249527c68a367b639d79bed45b3e3&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







