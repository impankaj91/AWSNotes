'use strict';

exports.handler = (event, context, callback) => {
    const request = event.Records[0].cf.request;
    const headers = request.headers;
    const uri = request.uri;

    if (uri.startsWith('/api')) {
        callback(null, request);
        return;
    }

    if (!uri.endsWith('/') && !uri.endsWith('.html')) {
        request.uri = '/';
        request.headers['host'] = [{ key: 'host', value: headers.host[0].value }];
        callback(null, request);
    } else {
        callback(null, request);
    }
};
