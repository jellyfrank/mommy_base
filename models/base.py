#!/usr/bin/python3
# @Time    : 2022-03-30
# @Author  : Kevin Kong (kfx2007@163.com)

from odoo import api, fields, models, _


class BaseModel(models.AbstractModel):

    _inherit="base"

    @api.model
    def read_group(self, domain, fields, groupby, offset=0, limit=None, orderby=False, lazy=True):
        res = super(BaseModel,self).read_group(
            domain, fields, groupby, offset=offset, limit=limit, orderby=orderby, lazy=lazy)
        for field_name in fields:
            field = self._fields[field_name]
            if field.compute and hasattr(field, 'group') and getattr(field, 'group') and field.type in ('integer','float','moneytary'):
                # need it add sum
                for group in res:
                    if '__domain' in group:
                        records = self.search(group['__domain'])
                        # [FIXME] only sum today.
                        group[field_name] = sum(getattr(record, field_name) for record in records)
        return res