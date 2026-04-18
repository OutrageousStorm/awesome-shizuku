/**
 * TypeScript definitions for Shizuku IPC
 * Provides type-safe access to Shizuku binder interface
 */

declare namespace Shizuku {
  interface ShizukuSystemServiceManager {
    checkPermission(permission: string): number;
    checkSelfPermission(permission: string): number;
    hasPermission(permission: string): boolean;
  }

  interface TransactListener {
    onTransactDone(transactCode: number, replies: Parcel): void;
  }

  interface IBinder {
    transact(code: number, data: Parcel, reply: Parcel | null, flags: number): boolean;
    queryLocalInterface(descriptor: string): IInterface | null;
    getInterfaceDescriptor(): string;
    isBinderAlive(): boolean;
  }

  interface IInterface {
    asBinder(): IBinder;
  }

  interface Parcel {
    writeData(data: any): void;
    readData(): any;
    createException(): Error | null;
  }

  interface ServiceManager {
    getService(name: string): IBinder | null;
    addService(name: string, service: IBinder, allowIsolated?: boolean): void;
  }

  function getSystemService(name: string): any;
  function checkPermission(permission: string): number;
  function registerUserService(descriptor: string, manager: () => IInterface): boolean;
}

export = Shizuku;
