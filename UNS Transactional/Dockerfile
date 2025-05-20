# Use NodeJS as the Builder
FROM node:18.16.1 as builder

# Install asyncapi Generator
RUN npm install -g @asyncapi/generator@1.9.12

# Copy in Asyncapi Files
COPY ./Components/ ./Components/
COPY ./Examples/ ./Examples/
COPY ./Messages/ ./Messages/
COPY ./asyncapi2.yaml ./asyncapi2.yaml

# Build static Site
RUN ag -i --force-write ./asyncapi2.yaml @asyncapi/html-template@v0.28.4 -o site

# Final Image
FROM nginx

# Copy Static site from builder
COPY --from=builder /site /usr/share/nginx/html

# Copy in additional files
# COPY ./drawings/ /usr/share/nginx/html/drawings/
# COPY ./B2MML_V0701_schemas/Custom/ /usr/share/nginx/html/json-validation-schemas/

# Labels
# LABEL org.opencontainers.image.source=""
LABEL org.opencontainers.image.title="Rhize MDH Async API Documentation"
LABEL org.opencontainers.image.vendor="Libre Technologies Inc https://www.libremfg.com/"