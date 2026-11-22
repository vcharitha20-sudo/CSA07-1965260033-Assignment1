def total_loss(km,db_per_km,connectors,splices):
    return km*db_per_km+0.5*connectors+0.1*splices
def margin(tx_dbm,rx_sensitivity_dbm,loss_db):
    return tx_dbm-loss_db-rx_sensitivity_dbm
LINKS=[('Floor to data hall, single-mode',0.7,0.35,4,2,-5.,-24.),('Floor to data hall, multimode',0.7,3.,4,2,-7.5,-17.),('Between buildings, single-mode',10,0.35,4,6,-5.,-24.),('Long haul, single-mode',40,0.35,4,10,-5.,-24.)]
for name,km,att,con,spl,tx,rx in LINKS:
    loss=total_loss(km,att,con,spl);m=margin(tx,rx,loss)
    print(f'{name}: loss {loss:.2f} dB margin {m:.2f} dB {"OK" if m>=3 else "FAIL"}')
print('Maximum km with 4 connectors, 6 splices:',(19-3-2-0.6)/0.35)
