FROM node:14

WORKDIR /app

COPY package.json ./
COPY package-lock.json ./
RUN npm install
RUN npm install react@18.3.1
RUN npm install axios@1.7.2
RUN npm install react-switch@7.0.0
RUN npm install react-router-dom@6.26.0
RUN npm install redux
RUN npm install react-redux
RUN npm install @chatscope/chat-ui-kit-react@2.0.3
RUN npm install @chatscope/chat-ui-kit-styles@1.4.0
RUN npm install @testing-library/jest-dom@5.17.0
RUN npm install @testing-library/react@13.4.0
RUN npm install @testing-library/user-event@13.5.0
RUN npm install web-vitals@2.1.4

CMD ["npm", "start"]