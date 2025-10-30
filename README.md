



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    1. RPC APIs:- Remote Procedure Calls
    1. WebSocket APIs:- Used JSON objects, two way communication
    1. REST API: - Most Popular
    

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

    1. The formatted resource is called a Representation in REST.
    1. Request should identify recourses by using URI
    1. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    1. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    1. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    1. Communication method in which the server completes every client request independently of all previous request.
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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UA6I2TQN%2F20251030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251030T225825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCGBnDMyS%2FUQzAbNLoaY1zmhis8R9j6IU%2Fle%2FukWS9qGwIgMz0QzJG%2Fz7YMxz0gsgnODssxFvSo%2BV7%2FNhV9IihMqr8qiAQI9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMCA36eq%2FEEIpbuN3ircAwMXFbcK1fhCax7qEeY35VZgNpetqfrhnsckyMzI9lrBgZmD6FId0qHIi3hcm4BhiM%2FAOYNz0TdgVZIeBiLzhhvE1cu6Q2u25w8HitfwmKBOGXymG%2FtiEh77h61419eF0GkeGJEObodloSSv8WF3usZqcecwb39lbjgApXJQxdawx%2BjRq3T%2BVcaRSCWgaLPeR1RedsGu1DQRXTs3gZoRTm2v%2Bl1lVsB2%2FOUhFkUH4f4onDGtDKQ8pIDW991YNcZPDk1Cw3FYUVHQ0b8W2p8nJALB2mWwG4EDal0beN0JW3O9T14OkEauyXMzuNWGCO213LJCDyEjgY3SXk%2FfVvNAPPvtBlvlOyVuAbuaDP4yaDURe%2BAcUnqtAZvZrB%2BENSDeLoDBXk5gZGhBQpx%2FVypLxYDHUSGTgh4DKM7C0Ac1vkjF05U944t%2BzMKAlAD5%2FhQLERtN1ae%2BwJHIagO0qr1SL2AHuTlKziskATGdBxRL%2F4nUeAmgxUAJiYqtRT5jxl6Xq5zlLwnYs1QN%2FH1%2BDSL6p%2FA27nM5JvOARMBpTCkU2OINMBPE9CrVyXCQtncjnbGb4Yq9xxn3gM46QPq5AOKjlC8w5chxUTomrYnpJ8dfoP2RhoA7JbPJgdmUugpEMInGj8gGOqUBwj2Yi2N%2BxdO7%2FJhDm9fJg5aOaniFs8Rz3j5zUhdZoNd3gyD%2B%2BjIeMoo0V6wW7EoZvzA7nGwyEqdII2VK5EuYIt9GgeiG%2BvSRS%2BWCG2vY1FbVd861LNMRLzBLTKBqPb%2FM%2B1IXH2MTdjlB0CdUJAk84TA3VOmidqZ835AEWlM9WRcSunN%2FyNZN7khg8Vexx3urltq6uOFABUV9y4BlQVqi9luGbqFx&X-Amz-Signature=3bc5646eb4e1e948e54e8677a230031c96dc082fa9bd01672b61f9ae9d94f034&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466UA6I2TQN%2F20251030%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251030T225825Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjED4aCXVzLXdlc3QtMiJHMEUCIQCGBnDMyS%2FUQzAbNLoaY1zmhis8R9j6IU%2Fle%2FukWS9qGwIgMz0QzJG%2Fz7YMxz0gsgnODssxFvSo%2BV7%2FNhV9IihMqr8qiAQI9%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDMCA36eq%2FEEIpbuN3ircAwMXFbcK1fhCax7qEeY35VZgNpetqfrhnsckyMzI9lrBgZmD6FId0qHIi3hcm4BhiM%2FAOYNz0TdgVZIeBiLzhhvE1cu6Q2u25w8HitfwmKBOGXymG%2FtiEh77h61419eF0GkeGJEObodloSSv8WF3usZqcecwb39lbjgApXJQxdawx%2BjRq3T%2BVcaRSCWgaLPeR1RedsGu1DQRXTs3gZoRTm2v%2Bl1lVsB2%2FOUhFkUH4f4onDGtDKQ8pIDW991YNcZPDk1Cw3FYUVHQ0b8W2p8nJALB2mWwG4EDal0beN0JW3O9T14OkEauyXMzuNWGCO213LJCDyEjgY3SXk%2FfVvNAPPvtBlvlOyVuAbuaDP4yaDURe%2BAcUnqtAZvZrB%2BENSDeLoDBXk5gZGhBQpx%2FVypLxYDHUSGTgh4DKM7C0Ac1vkjF05U944t%2BzMKAlAD5%2FhQLERtN1ae%2BwJHIagO0qr1SL2AHuTlKziskATGdBxRL%2F4nUeAmgxUAJiYqtRT5jxl6Xq5zlLwnYs1QN%2FH1%2BDSL6p%2FA27nM5JvOARMBpTCkU2OINMBPE9CrVyXCQtncjnbGb4Yq9xxn3gM46QPq5AOKjlC8w5chxUTomrYnpJ8dfoP2RhoA7JbPJgdmUugpEMInGj8gGOqUBwj2Yi2N%2BxdO7%2FJhDm9fJg5aOaniFs8Rz3j5zUhdZoNd3gyD%2B%2BjIeMoo0V6wW7EoZvzA7nGwyEqdII2VK5EuYIt9GgeiG%2BvSRS%2BWCG2vY1FbVd861LNMRLzBLTKBqPb%2FM%2B1IXH2MTdjlB0CdUJAk84TA3VOmidqZ835AEWlM9WRcSunN%2FyNZN7khg8Vexx3urltq6uOFABUV9y4BlQVqi9luGbqFx&X-Amz-Signature=9bfa297adcd7e444b4ca8cbc83c137013411923cb9350c83d2394f9f72cf9dbf&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  1. Atom publishing Protocol
  1. RSS ( Really Simple Syndication) 


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





Test Github-Notion synch



