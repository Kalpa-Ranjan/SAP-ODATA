



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRJCXXL3%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T020907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIEqcwmHv9k2gZMO1t9zhBDKFPfqZzkAzF6nONQAoS%2ByzAiEA7820OwHQwlBg1sOacytXMVv2kuBYoX10gua9Mp8EQTkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDAkdCqjft7SGTu2BoSrcA7kt36UnPtIj%2BZXEXHwJC6c0czucat9ISt8XRvoPyqK0OIa3FuPeLuvyRyCbs6fV9JhX7CuO1c6g7jl8ymSeeC5nOcYCuIkJ6XSxnkRKO2lWS20USXwvij%2FeD95gktnC1z9OVwvm%2FO7Gv6ITg4kd3GxdLsOodSLxxmxNyl%2FoVIbaMYVE0YyU1XWvoXJZdTdbchTw2MaH%2FdUNygc1bgTDAO5Y5auTw0%2FYwpa5YtTqv4NWOLoRYUrcH5XtbCzowO8rFQm0CeGhPbuGbftY2X6nl0kKC%2Blta729nkYjPjNBIjJsSC8fFwtnkP%2FEmq9IcqWHzw%2BkaqT7F%2FYOnjLw1Fm8WydGj6JfBFxyEhlMisqr%2BgfapUtaCT%2FBm2XLlhr9rQw2uN9BCaqUpHDWNc4LTaK5Fr2rI%2B46zp4q%2FYONIa%2FtB2gR33jOgtivX7AbjopNF6yIC0dhI1kD3Qyc7w52a6u1uKUA4xlblgLrNcOaMxtV6sxB53dbpLrQ7IOKs%2B7qA7HVELjX4ftImPpl3YdQpfKU%2FQBuupeVT5lsxEH9E3xKJ0WYuz8eQselrB2GRVMCvFTIPw6WrRSvKwnJTToANIL%2FaH9iquBvT07H3kAIkVyPi6Qq7iU86pXc7sevhfxdMPvnj9MGOqUBZFrKl3uUdqqj6pyVlVkBCvcDVlqOsggm8dr0BrB6UJXTb%2FxdQynhqlTiQAzU1TdEZY4DiKX1M56lE02zvPtuYQawP98jRFpSKveIk3o7R5GIxOPjjfurwXzthj2d73og7Q3e5gSsi1AnjNXSp9bpFhX02ZDYgUK7fkGyOnTdXV3gkpu2HMInFYb3RLXPM8QPf%2BPlodfhHXQcu6TsAiEIZMy9aFU5&X-Amz-Signature=cf7acae97470ab85a672ffc49c6cb9319059c9dec7840b21bf7bed23b49c33b0&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YRJCXXL3%2F20260725%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260725T020907Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEEgaCXVzLXdlc3QtMiJHMEUCIEqcwmHv9k2gZMO1t9zhBDKFPfqZzkAzF6nONQAoS%2ByzAiEA7820OwHQwlBg1sOacytXMVv2kuBYoX10gua9Mp8EQTkq%2FwMIERAAGgw2Mzc0MjMxODM4MDUiDAkdCqjft7SGTu2BoSrcA7kt36UnPtIj%2BZXEXHwJC6c0czucat9ISt8XRvoPyqK0OIa3FuPeLuvyRyCbs6fV9JhX7CuO1c6g7jl8ymSeeC5nOcYCuIkJ6XSxnkRKO2lWS20USXwvij%2FeD95gktnC1z9OVwvm%2FO7Gv6ITg4kd3GxdLsOodSLxxmxNyl%2FoVIbaMYVE0YyU1XWvoXJZdTdbchTw2MaH%2FdUNygc1bgTDAO5Y5auTw0%2FYwpa5YtTqv4NWOLoRYUrcH5XtbCzowO8rFQm0CeGhPbuGbftY2X6nl0kKC%2Blta729nkYjPjNBIjJsSC8fFwtnkP%2FEmq9IcqWHzw%2BkaqT7F%2FYOnjLw1Fm8WydGj6JfBFxyEhlMisqr%2BgfapUtaCT%2FBm2XLlhr9rQw2uN9BCaqUpHDWNc4LTaK5Fr2rI%2B46zp4q%2FYONIa%2FtB2gR33jOgtivX7AbjopNF6yIC0dhI1kD3Qyc7w52a6u1uKUA4xlblgLrNcOaMxtV6sxB53dbpLrQ7IOKs%2B7qA7HVELjX4ftImPpl3YdQpfKU%2FQBuupeVT5lsxEH9E3xKJ0WYuz8eQselrB2GRVMCvFTIPw6WrRSvKwnJTToANIL%2FaH9iquBvT07H3kAIkVyPi6Qq7iU86pXc7sevhfxdMPvnj9MGOqUBZFrKl3uUdqqj6pyVlVkBCvcDVlqOsggm8dr0BrB6UJXTb%2FxdQynhqlTiQAzU1TdEZY4DiKX1M56lE02zvPtuYQawP98jRFpSKveIk3o7R5GIxOPjjfurwXzthj2d73og7Q3e5gSsi1AnjNXSp9bpFhX02ZDYgUK7fkGyOnTdXV3gkpu2HMInFYb3RLXPM8QPf%2BPlodfhHXQcu6TsAiEIZMy9aFU5&X-Amz-Signature=7ce6a362fc367371df31be999cc110f32290b51f209857dbad150deff47b130a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







