



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7LF6OAV%2F20261101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261101T060741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG26pwVirYdqzWQikcPS32RNoBXcB3ABXB7Sd%2FpI4xe3AiAYiep3FXAZlbWZO7%2B2%2F48GANEWoMULQDdQ7DYVT2iQBSr%2FAwheEAAaDDYzNzQyMzE4MzgwNSIMzt%2BlSLoh7NTPOuMbKtwDEwjDiQOVqvYk%2FJQpnp9zzpHovY8kyXR9Af3dJfTFzm%2FHlzP7anfR4OZAGwRC5sFx9K9re4YnS7beVrRCXsRxLZpkv7tZMSVMiRtas7io29gJNzSi7zlsAEwZ2babIm7wybSFWrU53Kc%2BUV0H6oUtR0RhJy0jIWOzdPYvL75lrikcrweVh8D1HYVgGZ2tLIQJlwyJGOdCvHtNNLSn2jA1w4Ls%2BMwK5msvHaehFSZgkKQ83XKbbfNb%2BNXefcviHjhHqUCKL%2BdVyKKJZs0dBWYUSqG37qZk%2FQdr0Hf%2BAniFyLsVABeLV2OOdP8tfpWOGCH7o4IFR7e6nBIuC7eTZtFx6wuF2R53RrCX%2FzyUocbhx2eQypOErrqDoRddIv9CdbHCXXzFyBA931Vsbpqy4mzwzHuRY828jzjlQX0c8ATBqdL2Mh5HJaWJ%2FxTG4sPEBUIyv2VA%2BjmFD2co7cZG%2B1ZkE02%2FgXu6F%2BVVLK8pZ1GGqUbDVL2vGD1SQZpTMES%2B3GnGsYvOs3LAwnSm5rZvRr3x7MPU9V%2Bv8FnDZbgP3R9R7TjksiaOkDzdtx6vZw7SZMkuSHkoy9aD9rdWS%2FxyOcUvvhUL%2Bb8gb6MgHh4DSFU7HQ%2B6nOkKw7AOJCJD6dwwvqSb1wY6pgEk%2F8%2FIehVPqOOMSSHSXTF6ahhNMrPIs0T%2B%2BW%2FkIlvt%2FsWZit0pXddxTCmgBm5hRUy%2BpDtnTQ0FoSS3KfVf%2BIIxHZklACwuuP%2Blc2gqGk%2FvBhOhXJW3IDuYtKlCllVEcS4BQZyC9F8FsdJ6YBD5tEJeOo8QwfzxiQp4%2FfTKsNuMkZs24nCPequZYNcxhjXSvuX7Ku8gq%2BACNffBOnoGMBU9l5ISv4N5&X-Amz-Signature=9b93b41adf90f26a21a2a5ade0ec8df5d866881f7a49c1039d5a508729bcc061&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466X7LF6OAV%2F20261101%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261101T060741Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIG26pwVirYdqzWQikcPS32RNoBXcB3ABXB7Sd%2FpI4xe3AiAYiep3FXAZlbWZO7%2B2%2F48GANEWoMULQDdQ7DYVT2iQBSr%2FAwheEAAaDDYzNzQyMzE4MzgwNSIMzt%2BlSLoh7NTPOuMbKtwDEwjDiQOVqvYk%2FJQpnp9zzpHovY8kyXR9Af3dJfTFzm%2FHlzP7anfR4OZAGwRC5sFx9K9re4YnS7beVrRCXsRxLZpkv7tZMSVMiRtas7io29gJNzSi7zlsAEwZ2babIm7wybSFWrU53Kc%2BUV0H6oUtR0RhJy0jIWOzdPYvL75lrikcrweVh8D1HYVgGZ2tLIQJlwyJGOdCvHtNNLSn2jA1w4Ls%2BMwK5msvHaehFSZgkKQ83XKbbfNb%2BNXefcviHjhHqUCKL%2BdVyKKJZs0dBWYUSqG37qZk%2FQdr0Hf%2BAniFyLsVABeLV2OOdP8tfpWOGCH7o4IFR7e6nBIuC7eTZtFx6wuF2R53RrCX%2FzyUocbhx2eQypOErrqDoRddIv9CdbHCXXzFyBA931Vsbpqy4mzwzHuRY828jzjlQX0c8ATBqdL2Mh5HJaWJ%2FxTG4sPEBUIyv2VA%2BjmFD2co7cZG%2B1ZkE02%2FgXu6F%2BVVLK8pZ1GGqUbDVL2vGD1SQZpTMES%2B3GnGsYvOs3LAwnSm5rZvRr3x7MPU9V%2Bv8FnDZbgP3R9R7TjksiaOkDzdtx6vZw7SZMkuSHkoy9aD9rdWS%2FxyOcUvvhUL%2Bb8gb6MgHh4DSFU7HQ%2B6nOkKw7AOJCJD6dwwvqSb1wY6pgEk%2F8%2FIehVPqOOMSSHSXTF6ahhNMrPIs0T%2B%2BW%2FkIlvt%2FsWZit0pXddxTCmgBm5hRUy%2BpDtnTQ0FoSS3KfVf%2BIIxHZklACwuuP%2Blc2gqGk%2FvBhOhXJW3IDuYtKlCllVEcS4BQZyC9F8FsdJ6YBD5tEJeOo8QwfzxiQp4%2FfTKsNuMkZs24nCPequZYNcxhjXSvuX7Ku8gq%2BACNffBOnoGMBU9l5ISv4N5&X-Amz-Signature=5ee28cc34851657970d15cef5d15c6fcbeac4e53cc9b93272f8eedde2cdacb3e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







