import { mergeApplicationConfig, ApplicationConfig, importProvidersFrom } from '@angular/core';
import { provideServerRendering } from '@angular/platform-server';
import { provideHttpClient } from '@angular/common/http';
import { appConfig } from './app.config';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

const serverConfig: ApplicationConfig = {
  providers: [
    provideServerRendering(),
    provideHttpClient(), // Provide HttpClient for the server
    importProvidersFrom(BrowserAnimationsModule) // Required for Angular Material
  ]
};

export const config = mergeApplicationConfig(appConfig, serverConfig);